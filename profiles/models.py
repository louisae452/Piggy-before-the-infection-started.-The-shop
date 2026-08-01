from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user__username}"


class PasswordResetLog(models.Model):
    # Code generated with AI to log password resets.
    requested_email = models.EmailField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f" Reset requested for {self.requested_email} at {self.timestamp}"
    # End of code generated wiht AI.