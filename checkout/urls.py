from django.urls import path
from . import views

app_name = 'checkoout'
urlpatterns = [
    path('', views.checkout, name='checkout'),
]