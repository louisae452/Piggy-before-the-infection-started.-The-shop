from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

# Adapter created to redirect allauth change_password  and email templates to profile template. Created with AI.
class CustomAccountAdapter(DefaultAccountAdapter):
    
    def get_password_change_redirect_url(self, request):
        """Redirects back to the profile dashboard after changing password."""
        return reverse('profiles:profile')
    
    def get_email_redirect_url(self, request):
        """Redirects back to the profile dashboard after adding, removing, or changing an email."""
        return reverse('profiles:profile')
    