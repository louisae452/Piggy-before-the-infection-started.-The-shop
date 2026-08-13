from . import views
from django.urls import path


app_name = 'profiles'

urlpatterns = [
    path('', views.profile, name='profile'),
]