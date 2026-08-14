from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm, EmailForm
from .models import Profile



# Create your views here.
@login_required
def profile(request):
    user_instance = request.user
    user_profile, created = Profile.objects.get_or_create(user=user_instance)
    userform = UserForm(instance=user_instance)
    profileform = ProfileForm(instance=user_profile)
    emailform = EmailForm(instance=user_instance)
    
    if request.method == "POST":
        if 'personalreset' in request.POST:
            userform = UserForm(data=request.POST, instance=user_instance)
            if userform.is_valid():
                userform.save()    
                return redirect('profiles:profile')
            #profileform = ProfileForm(instance=user_profile)
            #emailform = EmailChangeForm(instance=user_instance)
            
        
            #userform = UserForm(instance=user_instance)
            #profileform = ProfileForm(instance=user_profile)
        elif 'shippingreset' in request.POST:
            profileform = ProfileForm(data=request.POST, instance=user_profile)
            if profileform.is_valid():
                profileform.save()
                return redirect('profiles:profile')
            #userform = UserForm(instance=user_instance)
            #emailform = EmailChangeForm(instance=user_instance)
    
    return render(
        request,
        "profiles/profile.html",
        {
            'userform': userform,
            'profileform': profileform,
            'emailform': emailform,
        }
    )


               