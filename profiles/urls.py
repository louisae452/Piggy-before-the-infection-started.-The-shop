from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
     path('', views.profile, name='profile'),
     path('order-detail/<int:order_id>/', views.past_order_detail,
          name='pastorderdetail'),
     path('order-history/<int:user_id>/', views.order_history,
          name='orderhistory'),
]
