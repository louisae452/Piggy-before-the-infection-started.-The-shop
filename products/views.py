from django.shortcuts import render
from django.db.utils import OperationalError, ProgrammingError

from .models import Homepage

# Create your views here.


def home_page(request):
    try:
        homepage = Homepage.objects.filter(is_active=True).select_related('top_left_href', 'top_right_href', 'bottom_left_href', 'bottom_right_href').first()
    except (OperationalError, ProgrammingError):
        homepage = None    
    
    context = {
        'homepage': homepage,
        }
    return render(request, "products/home.html", context)
