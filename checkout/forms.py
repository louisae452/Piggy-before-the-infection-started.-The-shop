from django import forms
from django.contrib.auth.models import User
from .models import Order

class UserForm(forms.ModelForm):
    save_name = forms.BooleanField(required=False, initial=False, label='Save name to my profile')
    class Meta:
       
        model = User
        fields = ('first_name', 'last_name',)
        
#
    
class OrderForm(forms.ModelForm):
    save_profile = forms.BooleanField(required=False, initial=False, label='Save address to my profile')
    class Meta:
        model = Order
        fields = ('phone_number', 'street_address1', 'street_address2', 'town', 'postcode', 'country',)