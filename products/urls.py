from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home'),
    path('allproducts/', views.all_products, name='allproducts'),
    path('<slug:slug>/', views.product_detail, name='productdetail'),
]
