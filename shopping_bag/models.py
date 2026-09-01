
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ShoppingBasket(models.Model):
    """
    Creates an instance of ShoppingBasket.
    Related to :model:`User`
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(
        max_length=40, null=True, blank=True, db_index=True)
    created_on = models.DateField(auto_now_add=True)


class ShopItems(models.Model):
    """
    Creates an instance of ShopItems
    Related to :model:`shopping_bag.ShoppingBasket`
    Related to :model:`products.Produt`
    """
    basket = models.ForeignKey(
        ShoppingBasket, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_on = models.DateField(auto_now_add=True)

    @property
    def subtotal(self):
        return self.product.price * self.quantity
