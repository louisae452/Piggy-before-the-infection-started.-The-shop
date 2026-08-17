
import sys
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import ShoppingBasket, ShopItems

# Create your views here.
# Helper function to retrieve or create basket. Created with A!.
def get_basket(request):
    if request.user.is_authenticated:
        basket, created = ShoppingBasket.objects.get_or_create(user=request.user)
    else:
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key
        basket, created = ShoppingBasket.objects.get_or_create(session_key=session_key)
        request.session['anonymous_basket_id'] = basket.id
        request.session.modified = True 
    return basket
# End of AI





# View to render shopping bag page.

def shopping_bag(request):
    basket = get_basket(request)
    items = basket.items.all().select_related('product')
    return render(
        request,
        "shopping_bag/shopping_bag.html",
        {
            'basket': basket,
            'items': items,
         }
    )

def add_to_bag(request, product_code):
    product = get_object_or_404(Product, code=product_code)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')
    basket = get_basket(request)
    item, item_created = ShopItems.objects.get_or_create(basket=basket, product=product, defaults={'quantity': quantity})
    if not item_created:
        item.quantity += quantity
        item.save()
    return redirect(redirect_url)
  
def update_bag(request, product_code):
    product = get_object_or_404(Product, code=product_code)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url', '/')
    basket = get_basket(request)
    item = get_object_or_404(ShopItems, basket=basket, product=product)
    item.quantity = quantity
    item.save()
    return redirect(redirect_url)

def remove_from_basket(request, product_code):
    product = get_object_or_404(Product, code=product_code)
    redirect_url = request.POST.get('redirect_url', '/')
    basket = get_basket(request)
    item = get_object_or_404(ShopItems, basket=basket, product=product)
    item.delete()
    return redirect(redirect_url)
    
        