from django.conf import settings
from django.db import models
from products.models import Product


class Order(models.Model):
    """
    Creates an instance of an order.
    Related to :model:`User`

    """
    user = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.SET_NULL,
                        null=True,
                        blank=True,
                        related_name='orders'
                    )
    full_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(blank=True, null=True)
    street_address1 = models.CharField(max_length=100, null=False, blank=False)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=50, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    basket_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    shipping = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    stripe_session_id = models.CharField(max_length=254, blank=True, null=True)
    stripe_pid = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=20, default='pending')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.date} {self.full_name}"


class OrderLineItem(models.Model):
    """
    Creates an instance of orderlineitem
    Related to :model:`checkout.Order`
    Related to :model:`proucts.Product`
    """
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    lineitem_total = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False)
