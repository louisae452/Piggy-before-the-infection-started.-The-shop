from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from checkout.models import Order
from .forms import EmailForm, ProfileForm, UserForm
from .models import Profile


@login_required
def profile(request):
    """
    Displays instances of :form:`profiles.UserForm`,
    :form:`profiles.EmailForm` and :form:`profiles.ProfileForm`
    **Context**
    ``userform``
        an instance of :form:`profiles.UserForm`
    ``profileform``
        an instance of :form:`profiles.ProfileForm`
    ``emailform``
        an instance of :form:`profilies.EmailForm`
    **Template**
    :template:`profiles.profile.html`
    """
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
                messages.success(
                    request,
                    "Your personal details have been updated."
                )
                return redirect('profiles:profile')
        elif 'shippingreset' in request.POST:
            profileform = ProfileForm(data=request.POST, instance=user_profile)
            if profileform.is_valid():
                profileform.save()
                messages.success(
                    request,
                    "Your shipping information has been updated"
                )
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


@login_required
def order_history(request, user_id):
    """
    Displays a queryset of :model:`checkout.Order`
    **Parameters**
    ``user_id``
        the user id of an instance of :model:`User`
    **Context**
    ``oder_list``
        a queryset of :model:`checkout.Order`
    ``user``
        an instance of :model:`User`

    **Template**
    :template:`profiles/order_history.html`
    """
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
    """
    Displays an instance of :model:`checkout.Order`
    **Parameters**
    ``order_id``
        the order_id of an instance of :model:`checkout.Order`
    **Context**
    ``user``
        an instance of :model:`User`
    '`order``
        an instance of :model:`checkout.Order`
    `order_items``
        a lsit of items in an instance of :model:`checkout.Order`
    """
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
