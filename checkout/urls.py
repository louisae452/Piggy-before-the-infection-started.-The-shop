from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
    path('success/', views.payment_success, name='payment_success'),
]
