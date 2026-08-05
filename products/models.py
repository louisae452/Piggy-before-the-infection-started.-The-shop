import os
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    """Categories model"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Group(models.Model):
    """Groups inside each category"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Product(models.Model):
    """Products model"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    code = models.CharField(max_length=10)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField(max_length=50, blank=True, null=True)


class Image(models.Model):
    """Model for products images"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=500)

    @property
    def image_name(self):
        return os.path.basename(self.image_url)

    def __str__(self):
        return f"{self.image_name} for {self.product.name}"


class Video(models.Model):
    """Model for sidebar videos"""
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    link = models.URLField(max_length=500)

    def __str__(self):
        return f"{self.name} for {self.product.name}"


class Rating(models.Model):
    """Rating of the product"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, blank=True)
    rating = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        if self.user:
            author = self.user.username
        else:
            author = "Verified user"
        return f"{self.product.name} by {author}"
