from . import views
from django.urls import path

app_name = 'products'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('allproducts/', views.all_products, name='allproducts'),
    path('plushes/', views.plushes, name='plushes'),
    path('prints/', views.prints, name='prints'),
    path('<slug:slug>/', views.product_detail, name='productdetail'),
    path('rateproduct/<slug:slug>/', views.rate_product, name='rateproduct'),
    path('updatereview/<int:id>/', views.update_review, name='updatereview'),
]
