from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Image



def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    if bag is None:
        bag = {}
    
    for product_code, quantity in bag.items():
        product = Product.objects.filter(code=product_code).first()
        total += quantity * product.price
        product_count += quantity
        main_image = Image.objects.filter(product=product, is_main=True).first()
        if not main_image:
            main_image = Image.objects.filter(product=product).first()
        bag_items.append({
            'product_code': product.code,
            'main_image': main_image,
            'quantity': quantity,
            'product': product,
            
        })
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }
    return context