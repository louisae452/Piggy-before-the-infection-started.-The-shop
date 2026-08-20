import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from products.models import Product
from profiles.models import Profile
from .forms import UserForm, OrderForm
from .models import Order, OrderLineItem
from shopping_bag.models import ShoppingBasket
from shopping_bag.context import bag_contents
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    user = request.user
    profile = None
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            pass
    if request.method == "POST":
        user_form = UserForm(request.POST, prefix='user')
        address_form = OrderForm(request.POST, prefix='address')
        if user_form.is_valid() and address_form.is_valid():
            order = address_form.save(commit=False)
            if  not user_form.cleaned_data.get('first_name') or not user_form.cleaned_data.get('last_name') or not address_form.cleaned_data.get('street_address1') or not address_form.cleaned_data.get('postcode'):
                messages.error(request, "Please fill out all required shipping fields.")
                return render(
                    request, 
                    "checkout/checkout.html",
                    {
                        'user_form': user_form, 
                        'address_form': address_form})
            
            
            
            if user.is_authenticated:
                # Save order.
                order.user = user 
            current_bag = bag_contents(request)
            order.basket_total = current_bag['items_total']  
            order.shipping = current_bag['delivery']
            order.grand_total = current_bag['total']
            f_name = user_form.cleaned_data['first_name'].strip()
            l_name = user_form.cleaned_data['last_name'].strip()
            order.full_name = f"{f_name} {l_name}"
            order.save()
            # Save lineitems:
            current_bag = bag_contents(request)
            for item in current_bag['items']:
                OrderLineItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    lineitem_total=item['product'].price * item['quantity']
                )
            if user.is_authenticated:
                # If update details checked.
                if user_form.cleaned_data.get('save_name'):
                    user.first_name = f_name
                    user.last_name = l_name
                    user.save()
                if address_form.cleaned_data.get('save_profile'):
                    try:
                        profile = Profile.objects.get(user=user)
                    except Profile.DoesNotExist:
                        profile = Profile(user=user)
                    profile.phone_number = address_form.cleaned_data['phone_number']
                    profile.street_address1 = address_form.cleaned_data['street_address1']
                    profile.street_address2 = address_form.cleaned_data.get('street_address2')
                    profile.town = address_form.cleaned_data['town']
                    profile.postcode = address_form.cleaned_data['postcode']
                    profile.country = address_form.cleaned_data.get('country')
                    profile.save()
            messages.success(request, "Address saved")
            try:
                stripe_total = int(float(order.grand_total * 100))
                checkout_session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=[{
                        'price_data': {
                            'currency': 'gbp',
                            'product_data': {
                                'name': f"Order #{order.id} Payment",
                            },
                            'unit_amount': stripe_total
                        },
                        'quantity': 1,
                    }],
                    mode='payment',
                    
                    # For localhost environment:
                    success_url=f'http://localhost:8000/checkout/success/?session_id={{CHECKOUT_SESSION_ID}}&order_id={order.id}',
                    cancel_url=f'http://localhost:8000/checkout/cancel/?order_id={order.id}',   
                )
                return redirect(checkout_session.url, code=303)
            except Exception as e:
                messages.error(request, f"Stripe error:{str(e)}")
                return redirect('checkout:checkout')
        else: 
            messages.error(request, "Form verification failed. Please, fill all the required fiedls")
            return render(
                request,
                "checkout/checkout.html",
                {
                    'user_form': user_form,
                    'address_form': address_form,
                }
            )        
                
                
                
           
    else:
        user_initial = {}
        profile_initial = {}
        if user.is_authenticated:
            user_initial = {'first_name': request.user.first_name, 'last_name': user.last_name, } 
            profile_initial = {}
            if profile:
                profile_initial = {
                    'phone_number': profile.phone_number,
                    'street_address1': profile.street_address1,
                    'town': profile.town,
                    'postcode': profile.postcode,
                    'country': profile.country,
                }                        
        user_form = UserForm(initial=user_initial, prefix='user')
        address_form = OrderForm(initial=profile_initial, prefix='address')
    return render(
        request,
        "checkout/checkout.html",
        {
            'user_form': user_form,
            'address_form': address_form,
                    
        }
    )
    
#### Probably delete!!!!  
def payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(
        request,
        "checkout/payment.html",
        {
            'order': order,
        })
    
def payment_success(request):
    session_id = request.GET.get('session_id')
    order_id = request.GET.get('order_id')
    if not session_id or not order_id:
        messages.error(request, "Invalid payment confirmation parameter string.")
        return redirect('products:allproducts')
    order = get_object_or_404(Order, id=order_id)
    try:
        session = stripe.checkout.Session.retrieve(session_id)
        if session.payment_status == 'paid':
            order.stripe_pid = session_id
            order.status = 'paid'
            order.save()
            order_items = order.lineitems.all()
            if order.user:
                ShoppingBasket.objects.filter(user_id=order.user.id).delete()
            else:
                session_key = request.session.session_key
                if session_key:
                    ShoppingBasket.objects.filter(session_key=session_key).delete()
            
            if 'bag' in request.session:
                del request.session['bag']
            return render(
                request,
                "checkout/success.html",
                {
                    'order': order,
                    'order_items': order_items,
                }
            )
        else:
            order.status = 'failed'
            order.save()
            return render(
                request, "checkout/error.html",
                {
                    'message': 'Payment authorisation failed',
                }
            )
    except Exception as e:
        return render(
            request,
            "checkout/error.html",
            {
                'message': str(e),
            }
        )
      
        