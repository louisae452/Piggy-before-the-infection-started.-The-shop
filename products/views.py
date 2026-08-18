from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.utils import OperationalError, ProgrammingError

from .models import Homepage, Product

# Create your views here.

# Show homepage. Ensure that homepage loads even if not active homepage.
def home_page(request):
    try:
        homepage = Homepage.objects.filter(is_active=True).select_related('top_left_href', 'top_right_href', 'bottom_left_href', 'bottom_right_href').first()
    except (OperationalError, ProgrammingError):
        homepage = None    
    
    context = {
        'homepage': homepage,
        }
    return render(request, "products/home.html", context)

# Showsa listing of all products.
def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    products_page = paginator.get_page(page_number)
    return render(
        request,
        "products/all_products.html",
        {
            'products_page': products_page,
        }
    )
def plushes(request):
    products = Product.objects.filter(group__category__slug='plushes')
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    products_page = paginator.get_page(page_number)
    return render(
        request,
        "products/plushes.html",
        {
            'products_page': products_page,
        }
    )    
    
# View to show product detail.
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(
        request,
        "products/product_detail.html",
        {
            'product': product,
        }
        
    )
    
    
    