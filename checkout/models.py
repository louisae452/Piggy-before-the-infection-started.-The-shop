from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(blank=True, null=True)
    street_address1 = models.CharField(max_length=100, null=True, blank=True)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
    def __str__ (self):
        return f"{self.date} {self.full_name}"
        
        
    
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    lineitem_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    
    

