from django.dispatch import receiver
from allauth.account.signals import user_logged_in, user_signed_up
from .models import ShoppingBasket, ShopItems


# Created witn  AI to merge guest and user baskets.
def execute_basket_merge(request, user):
    """
    Helper function to safely locate the anonymous guest basket 
    and merge its products into the logged-in user's basket.
    """
    # 1. Fetch the persistent database ID backup from the session dict
    anonymous_basket_id = request.session.get('anonymous_basket_id')
    
    if not anonymous_basket_id:
        return

    try:
        # 2. Find the guest basket directly by its persistent Primary Key ID
        guest_basket = ShoppingBasket.objects.get(id=anonymous_basket_id)
        
        # 3. Get or create the user's permanent primary basket
        user_basket, created = ShoppingBasket.objects.get_or_create(user=user)
        
        # 4. Pull all items belonging to the guest basket
        guest_items = ShopItems.objects.filter(basket=guest_basket)
        
        for item in guest_items:
            # Check if this item already exists in the user's permanent basket
            existing_user_item = ShopItems.objects.filter(basket=user_basket, product=item.product).first()
            
            if existing_user_item:
                existing_user_item.quantity += item.quantity
                existing_user_item.save()
                item.delete()  # Clean up duplicate item row
            else:
                item.basket = user_basket  # Transfer ownership to user
                item.save()
        
        # 5. Clean up the empty guest basket shell and session markers
        guest_basket.delete()
        
        if 'anonymous_basket_id' in request.session:
            del request.session['anonymous_basket_id']
            request.session.modified = True
        
    except ShoppingBasket.DoesNotExist:
        # Fallback if the basket was already cleaned up or deleted
        pass


# Allauth specific receivers
@receiver(user_logged_in)
def merge_guest_basket_on_login(sender, request, user, **kwargs):
    execute_basket_merge(request, user)

@receiver(user_signed_up)
def merge_guest_basket_on_signup(sender, request, user, **kwargs):
    execute_basket_merge(request, user)
# End of AI.