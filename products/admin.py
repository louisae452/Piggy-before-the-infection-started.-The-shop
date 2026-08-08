from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Group, Product, Image, Video, Rating, Homepage, HomepageImage, HomepageVideo, Href

# Products models


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}


class ProductImageInLine(admin.TabularInline):
    model = Image
    extra = 2


class ProductVideoInLine(admin.TabularInline):
    model = Video
    extra = 2


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = ('code', 'name', 'group', 'price')
    search_fields = ('name', 'code', 'description')
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)
    inlines = [ProductImageInLine, ProductVideoInLine]


@admin.register(Rating)
class RatingAdmin(SummernoteModelAdmin):
    list_display = ('product', 'user', 'rating')
    search_fields = ('product__name', 'user__username')
    summernote_fields = ('comment',)


# Homepage models

@admin.register(HomepageImage)
class HomepageImageAdmin(admin.ModelAdmin):
    list_display = ['image_name']
    search_fields = ['image_name']


@admin.register(HomepageVideo)
class HomepageVideoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
@admin.register(Href)
class HrefAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
