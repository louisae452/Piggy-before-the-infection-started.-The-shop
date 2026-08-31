from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.functions import Cast
from django.core.exceptions import PermissionDenied
from django.db.utils import OperationalError, ProgrammingError
from django.contrib import messages
from django.db.models import Avg, FloatField
from .models import Homepage, Product, Rating
from .forms import RatingForm



# Show homepage. Ensure that homepage loads even if not active homepage.
def home_page(request):
    try:
        homepage = Homepage.objects.filter(is_active=True).select_related(
            'top_left_href',
            'top_right_href',
            'bottom_left_href',
            'bottom_right_href').first()
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


def prints(request):
    products = Product.objects.filter(group__category__slug='3d-prints')
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    products_page = paginator.get_page(page_number)
    return render(
        request,
        "products/prints.html",
        {
            'products_page': products_page,
        }
    )


# View to show product detail.
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    ratings = Rating.objects.filter(product=product)
    average = ratings.aggregate(rating_avg=Avg(Cast('rating',
                                output_field=FloatField())))
    if average['rating_avg'] is not None:
        rating_average = round(average['rating_avg'], 1)
    else:
        rating_average = 0
    paginator = Paginator(ratings, 2)
    page_number = request.GET.get('page')
    ratings_page = paginator.get_page(page_number)
    return render(
        request,
        "products/product_detail.html",
        {
            'product': product,
            'rating_average': rating_average,
            'ratings': ratings,
            'ratings_page': ratings_page,
        }
    )


# View to create a rating   .

def rate_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == "POST":
        rating_form = RatingForm(data=request.POST)
        stars = request.POST.get('rating')
        if not stars or stars == "":
            messages.error(request, 'Please select a star rating')
            return render(
                request,
                "products/rate_product.html",
                {
                    'rating_form': rating_form,
                    'product': product
                }
            )
        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.product = product
            rating.rating = stars
            if request.user.is_authenticated:
                rating.user = request.user
            else:
                rating.user = None
            rating.save()
            messages.success(request, 'Rating added successfully')
            return redirect('products:productdetail', slug=slug)
        
    else:        
        rating_form = RatingForm()
    return render(
        request,
        "products/rate_product.html",
        {
            'rating_form': rating_form,
            'product': product
        }
        
        )


# View to update or delete review.

def update_review(request, id):
    rating = get_object_or_404(Rating, id=id)
    if rating.user != request.user:
        raise PermissionDenied('You do not have permission to rate this review')
    product = rating.product
    if request.method == "POST":
        action = request.POST.get('action')
        if action == 'delete':
            rating.delete()
            messages.success(request, 'Review successfully deleted')
            return redirect('products:productdetail', slug=product.slug)
        rating_form = RatingForm(data=request.POST, instance=rating)
        if rating_form.is_valid():
            new_rating = rating_form.save(commit=False)
            star_value = request.POST.get('rating')
            if star_value:
                new_rating.rating = str(star_value).strip()
            new_rating.save()
            messages.success(request, 'Review successfully updated')
            return redirect('products:productdetail', slug=product.slug)
    else:
        rating_form = RatingForm(instance=rating)
    return render(
        request,
        "products/update_review.html",
        {
            'product': product,
            'rating': rating,
            'rating_form': rating_form,
        }
    )
