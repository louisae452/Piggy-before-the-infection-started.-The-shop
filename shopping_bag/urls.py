from . import views
from django.urls import path

app_name = 'shopping_bag'

urlpatterns = [
    path('', views.shopping_bag, name='shoppingbag'),
    path('add/<str:product_code>/', views.add_to_bag, name='addtobag'),
    path('update/<str:product_code>/', views.update_bag, name='updatebag'),
    
]