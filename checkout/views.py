from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from products.models import Product
from profiles.models import Profile
from .forms import UserForm, OrderForm
# Create your views here.


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
            
            if user.is_authenticated:
                # Save order.
                order.user = user   
            f_name = user_form.cleaned_data['first_name'].strip()
            l_name = user_form.cleaned_data['last_name'].strip()
            order.full_name = f"{f_name} {l_name}"
            order.save()
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
            return redirect('checkout:payment')
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
    
    
def payment(request):
    return render(request, "checkout/payment.html")