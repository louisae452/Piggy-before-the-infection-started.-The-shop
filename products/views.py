from django.shortcuts import render, get_object_or_404
from .models import Homepage

# Create your views here.


def home_page(request):
    homepage = get_object_or_404(Homepage.objects.select_related('top_left_href', 'top_right_href', 'bottom_left_href', 'bottom_right_href'), is_active=True)
    context = {
        'homepage': homepage,
        }
    return render(request, "products/home.html", context)
