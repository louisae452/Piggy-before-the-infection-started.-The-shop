from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
class OrderlineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    extra = 0
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderlineItemAdminInLine]
    
    
                      
                  
                      
                      
                      
                      
                      