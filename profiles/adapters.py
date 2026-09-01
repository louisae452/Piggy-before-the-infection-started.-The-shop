from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

# Adapter created to redirect allauth changepassword template to profile template. Created with AI.
class CustomAccountAdapter(DefaultAccountAdapter):
    
    def get_password_change_redirect_url(self, request):
        # Redirect directly to your profile layout url name
        return reverse('profiles:profile')