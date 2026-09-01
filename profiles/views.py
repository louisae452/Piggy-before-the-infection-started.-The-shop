from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from allauth.account.views import EmailView
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .forms import UserForm, ProfileForm, EmailForm
from .models import Profile
from checkout.models import Order


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
                messages.success(request, "Your personal details have been updated.")
                return redirect('profiles:profile')
        elif 'shippingreset' in request.POST:
            profileform = ProfileForm(data=request.POST, instance=user_profile)
            if profileform.is_valid():
                profileform.save()
                messages.success(request, "Your shipping information has been updated")
                return redirect('profiles:profile')
    return render(
        request,
        "profiles/profile.html",
        {
            'userform': userform,
            'profileform': profileform,
            'emailform': emailform,
        }
    )

# View to see user's order history.
@login_required
def order_history(request, user_id):
    if request.user.id != int(user_id):
        raise PermissionDenied
    user = request.user
    order_list = Order.objects.filter(user_id=user_id).order_by('-date')
    return render(
        request,
        "profiles/order_history.html",
        {
            'order_list': order_list,
            'user': user,
        }
    )


@login_required
def past_order_detail(request, order_id, ):
    user = request.user
    order = get_object_or_404(Order, id=order_id)
    if not order.user or order.user != user:
        raise PermissionDenied
    order_items = order.lineitems.all()
    return render(
        request,
        "profiles/past_order_detail.html",
        {
            'user': user,
            'order': order,
            'order_items': order_items,
        }
    )

