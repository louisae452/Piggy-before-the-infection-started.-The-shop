from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

# Adapter created to redirect allauth change_password  and email templates to profile template. Created with AI.
class CustomAccountAdapter(DefaultAccountAdapter):
    
    def get_password_change_redirect_url(self, request):
        """Redirects back to the profile dashboard after changing password."""
        return reverse('profiles:profile')
    
    # def get_email_redirect_url(self, request):
    #    """Redirects back to the profile dashboard after adding, removing, or changing or resending verification."""
    #    return reverse('profiles:profile')
    
    def get_login_redirect_url(self, request):
        """Redirects back to the profile dashboard immediately after adding a new email address."""
        return reverse('profiles:profile')
    
    def get_email_confirmation_redirect_url(self, request):
        """
        Handles the redirect immediately after a user clicks the 
        verification link inside their email inbox.
        """
        return reverse('profiles:profile')