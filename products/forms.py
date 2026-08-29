from django import forms
from .models import Rating, STARS


class RatingForm(forms.ModelForm):
    
    class Meta:
        model = Rating
        fields = ('title', 'comment')