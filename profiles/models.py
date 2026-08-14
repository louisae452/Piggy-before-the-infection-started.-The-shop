from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(blank=True, null=True)
    street_address1 = models.CharField(max_length=100, null=True, blank=True)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}"


class PasswordResetLog(models.Model):
    # Code generated with AI to log password resets.
    requested_email = models.EmailField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f" Reset requested for {self.requested_email} at {self.timestamp}"
    # End of code generated wiht AI.