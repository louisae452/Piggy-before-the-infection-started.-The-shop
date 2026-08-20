from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    # path('payment/<int:order_id>/', views.payment, name='payment'),
    path('success/', views.payment_success, name='payment_success'),
    
]