from django import forms
from django.contrib.auth.models import User
from .models import Order


class UserForm(forms.ModelForm):
    save_name = forms.BooleanField(required=False, initial=False, label='Save name to my profile')

    class Meta:
       
        model = User
        fields = ('first_name', 'last_name',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
  
  
        
class OrderForm(forms.ModelForm):
    save_profile = forms.BooleanField(required=False, initial=False, label='Save address to my profile')
    
    class Meta:
        model = Order
        fields = ('phone_number', 'email', 'street_address1', 'street_address2', 'town', 'postcode', 'country',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['street_address1'].required = True
        self.fields['town'].required = True
        self.fields['postcode'].required = True