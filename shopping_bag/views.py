from django.shortcuts import get_object_or_404, redirect, render
from products.models import Product
from .models import ShoppingBasket, ShopItems


def get_basket(request):
    """
    Helper function to retrieve or create a basket.
    Created with AI
    """
    if request.user.is_authenticated:
        basket, created = ShoppingBasket.objects.get_or_create(
            user=request.user)
    else:
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key
        basket, created = ShoppingBasket.objects.get_or_create(
            session_key=session_key)
        request.session['anonymous_basket_id'] = basket.id
        request.session.modified = True
    return basket


def shopping_bag(request):
    """
    Displays shopping basket.
    **Context**
    ``basket``
        an instance of :model:`shopping_bag.ShoppingBasket`
    ``items``
        a queriset of :model:`shopping_bag.ShopItems`
    **Template**
    :template:`shopping_bag/shopping_bag.html`
    """
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
    """"
    Adds an item to the basket
    **Parameters**
    ``product_code``
        the code of an instance of :model:`products.Product`
    **POST parameters**
    ``quantity``
        the number of units to add.
    ``redirect_url``
        url path to follow after successful addition to basket.
    """
    product = get_object_or_404(Product, code=product_code)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')
    basket = get_basket(request)
    item, item_created = ShopItems.objects.get_or_create(
        basket=basket, product=product, defaults={'quantity': quantity})
    if not item_created:
        item.quantity += quantity
        item.save()
    return redirect(redirect_url)


def update_bag(request, product_code):
    """
    Updates the quantity of an existing item in the basket.
    **Parameters**
    ``product_code``
        the code of an instance of :model:`products.Product`
    **POST Parameters**
    ``quantity``
        the new number of units of a product in the basket
    ``redirect_url``
        url path to follow after successful basket update
    """
    product = get_object_or_404(Product, code=product_code)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url', '/')
    basket = get_basket(request)
    item = get_object_or_404(ShopItems, basket=basket, product=product)
    item.quantity = quantity
    item.save()
    return redirect(redirect_url)


def remove_from_basket(request, product_code):
    """
    Removes an item from the basket.
    **Parameters**
    ``product_code``
        the code for an instance of :model:`products.Product`
    **POST Parameters**
    ``redirect_url``
        the url path to follow after successful removal from basket.
    """
    product = get_object_or_404(Product, code=product_code)
    redirect_url = request.POST.get('redirect_url', '/')
    basket = get_basket(request)
    item = get_object_or_404(ShopItems, basket=basket, product=product)
    item.delete()
    return redirect(redirect_url)
