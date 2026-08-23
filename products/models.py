import os
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse, NoReverseMatch


# Products models.


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
    
    def __str__(self):
        return self.name

class Video(models.Model):
    """Model for sidebar videos"""
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='media/products/', blank=True, null=True)
    link = models.URLField(max_length=500)

    def __str__(self):
        return self.name

class Href(models.Model):
    name = models.CharField(max_length=100)
    url_name = models.URLField(max_length=225)

    def __str__(self):
        return self.name
   

    



class Product(models.Model):
    """Products model"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    code = models.CharField(max_length=10)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # link = models.URLField(max_length=500, blank=True, null=True)
    character_link = models.ForeignKey(Href, on_delete=models.SET_NULL, null=True, blank=True)
    videos = models.ManyToManyField(Video, blank=True, related_name='products')
    
    @property
    def main_image(self):
        return self.image_set.filter(is_main=True).first()
    
    def __str__(self):
        return self.name
    



class Image(models.Model):
    """Model for products images"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/products/')
    is_main = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.image_name} for {self.product.name}"


STARS = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))

class Rating(models.Model):
    """Rating of the product"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, blank=True)
    
    rating = models.CharField(choices=STARS, blank=True, null=True)
    title = models.CharField(max_length=100, null=True)
    comment = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)


    def __str__(self):
        if self.user:
            author = self.user.username
        else:
            author = "Verified user"
        return f"{self.product.name} by {author}"

# Homepage models.


class HomepageImage(models.Model):
    """Holds images to be used in the homepage"""
    image_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='homepage/', default='default_image')
    
    def __str__(self):
        return self.image_name

    

    




    
    
class Homepage(models.Model):
    """ Model to show the homepages."""
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    top_right = models.ForeignKey(HomepageImage, on_delete=models.SET_NULL,
                                  null=True, blank=True,
                                  related_name="toprightslot")
    top_right_title = models.CharField(max_length=100, blank=True, null=True)
    top_right_button = models.CharField(max_length=50, blank=True, null=True)
    top_right_href = models.ForeignKey(Href, on_delete=models.SET_NULL,
                                       blank=True, null=True,
                                       related_name="toprighthref")
    top_left = models.ForeignKey(HomepageImage, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name="topleftslot")
    top_left_title = models.CharField(max_length=100, blank=True, null=True)
    top_left_button = models.CharField(max_length=50, blank=True, null=True)
    top_left_href = models.ForeignKey(Href, on_delete=models.SET_NULL,
                                      blank=True, null=True,
                                      related_name="toplefthref")
    bottom_right = models.ForeignKey(HomepageImage, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name="bottomrightslot")
    bottom_right_title = models.CharField(max_length=100, blank=True, null=True)
    bottom_right_button = models.CharField(max_length=50, blank=True, null=True)
    bottom_right_href = models.ForeignKey(Href, on_delete=models.SET_NULL,
                                          blank=True, null=True,
                                          related_name="bottomrighthref")
    bottom_left = models.ForeignKey(HomepageImage, on_delete=models.SET_NULL,
                                    null=True, blank=True,
                                    related_name="bottomleftslot")
    bottom_left_title = models.CharField(max_length=100, blank=True, null=True)
    bottom_left_button = models.CharField(max_length=50, blank=True, null=True)
    bottom_left_href = models.ForeignKey(Href, on_delete=models.SET_NULL,
                                         blank=True, null=True,
                                         related_name="bottomlefthref")
    video1 = models.ForeignKey(Video, on_delete=models.SET_NULL,
                               null=True, blank=True,
                               related_name="video1slot")
    video2 = models.ForeignKey(Video, on_delete=models.SET_NULL,                              
                               null=True, blank=True,
                               related_name="video2slot")

    def __str__(self):
        return self.name




