from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)
        
# Form to require password to change email. From AI.
class EmailChangeForm(forms.ModelForm):
    current_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Current Password")

    class Meta:
        model = User
        fields = ['email']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_current_password(self):
        password = self.cleaned_data.get('current_password')
        if not self.user.check_password(password):
            raise forms.ValidationError("Incorrect password. Please try again.")
        return password
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number', 'street_address1', 'street_address2', 'town', 'postcode', 'country',)