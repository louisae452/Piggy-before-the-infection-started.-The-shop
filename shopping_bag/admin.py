from django.contrib import admin
from .models import ShopItems, ShoppingBasket

# Register your models here.


class ShopItemsInline(admin.TabularInline):
    model = ShopItems
    extra = 2


@admin.register(ShoppingBasket)
class ShoppingBasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_on')
    search_fields = ('user__username',)  
    inlines = [ShopItemsInline]
