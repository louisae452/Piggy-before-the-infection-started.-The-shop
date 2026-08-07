from django.shortcuts import render, get_object_or_404
from .models import Homepage

# Create your views here.


def home_page(request):
    homepage = get_object_or_404(Homepage, is_active=True)
    context = {
        'homepage': homepage,
        }
    return render(request, "products/home.html", context)
