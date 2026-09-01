from django.urls import path
from . import views

app_name = 'shopping_bag'

urlpatterns = [
    path('', views.shopping_bag, name='shoppingbag'),
    path('add/<str:product_code>/', views.add_to_bag, name='addtobag'),
    path(
         'remove/<str:product_code>/',
         views.remove_from_basket,
         name='removefrombasket'
        ),
    path('update/<str:product_code>/', views.update_bag, name='updatebag'),
]
