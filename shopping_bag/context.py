from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from products.models import Product, Image
from .models import ShoppingBasket, ShopItems



def bag_contents(request):
    items = []
    total = 0
    items_total = 0.00
    product_count = 0
    if request.user.is_authenticated:
        basket, created = ShoppingBasket.objects.get_or_create(user=request.user)
    else: 
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key
        basket, created = ShoppingBasket.objects.get_or_create(session_key=session_key)
        
    db_items = basket.items.all().select_related('product')
    for item in db_items:
        product = item.product
        main_image = Image.objects.filter(product=product, is_main=True).first()
        total += item.subtotal
        product_count += item.quantity
        if not main_image:
            main_image = Image.objects.filter(product=product).first()
        
        items.append({
            'product_code': product.code,
            'quantity': item.quantity,
            'subtotal': item.subtotal, 
            'product': product,
               
            'main_image': main_image,
        })
    items_total = total
    delivery = settings.DELIVERY_CHARGE
    total = float(total) + float(delivery)   
    
    context = {
        'items': items,
        'items_total': items_total,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
    }
    return context