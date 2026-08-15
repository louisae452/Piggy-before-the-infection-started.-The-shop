from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ShoppingBasket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    
    
    
class ShopItems(models.Model):
    basket = models.ForeignKey(ShoppingBasket, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_on = models.DateField(auto_now_add=True)
    
    @property
    def subtotal(self):
        return self.product.price * self.quantity