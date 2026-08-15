
import sys
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import ShoppingBasket, ShopItems

# Create your views here.
# View to render shopping bag page.
@login_required
def shopping_bag(request):
    basket, created = ShoppingBasket.objects.get_or_create(user=request.user)
    items = basket.items.all().select_related('product')
    return render(
        request,
        "shopping_bag/shopping_bag.html",
        {
            'basket': basket,
            'items': items,
         }
    )

@login_required    
def add_to_bag(request, product_code):
    product = get_object_or_404(Product, code=product_code)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')
    basket, created = ShoppingBasket.objects.get_or_create(user=request.user)
    item, item_created = ShopItems.objects.get_or_create(basket=basket, product=product, defaults={'quantity': quantity})
    if not item_created:
        item.quantaity += quantity
        item.save()
    return redirect(redirect_url)

@login_required    
def update_bag(request, product_code):
    product = get_object_or_404(Product, code=product_code)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url', '/')
    basket = get_object_or_404(ShoppingBasket, user=request.user)
    item = get_object_or_404(ShopItems, basket=basket, product=product)
    item.quantity = quantity
    item.save()
    return redirect(redirect_url)

@login_required
def remove_from_basket(request, product_code):
    product = get_object_or_404(Product, code=product_code)
    redirect_url = request.POST.get('redirect_url', '/')
    basket = get_object_or_404(ShoppingBasket, user=request.user)
    item = get_object_or_404(ShopItems, basket=basket, product=product)
    item.delete()
    return redirect(redirect_url)
    
        