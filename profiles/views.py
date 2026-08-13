from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm, EmailChangeForm
from .models import Profile



# Create your views here.
@login_required
def profile(request):
    user_instance = request.user
    userform = UserForm(instance=user_instance)
    user_profile, created = Profile.objects.get_or_create(user=user_instance)
    profileform = ProfileForm(instance=user_profile)
    emailform = EmailChangeForm(user=user_instance, instance=user_instance)
    
    return render(
        request,
        "profiles/profile.html",
        {
            'userform': userform,
            'profileform': profileform,
            'emailform': emailform,
        }
    )


               