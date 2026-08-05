import os
from django.contrib.auth.models import User
from django.db import models

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

# Homepage models.


class HomepageImage(models.Model):
    """Holds images to be used in the homepage"""
    image_url = models.URLField(max_length=500)

    @property
    def image_name(self):
        return os.path.basename(self.image_url)

    def __str__(self):
        return self.image_name


class HomepageVideo(models.Model):
    """Holds videos to be used in the homepage"""
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=500)

    def __str__(self):
        return self.name


class Homepage(models.Model):
    """ Model to show the homepages."""
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    top_right = models.ForeignKey(HomepageImage, on_delete=models.SET_NULL,
                                  null=True, blank=True,
                                  related_name="toprightslot")
    top_left = models.ForeignKey(HomepageImage, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name="topleftslot")
    bottom_right = models.ForeignKey(HomepageImage, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name="bottomrightslot")
    bottom_left = models.ForeignKey(HomepageImage, on_delete=models.SET_NULL,
                                    null=True, blank=True,
                                    related_name="bottomleftslot")
    video1 = models.ForeignKey(HomepageVideo, on_delete=models.SET_NULL,
                               null=True, blank=True,
                               related_name="video1slot")
    video2 = models.ForeignKey(HomepageVideo, on_delete=models.SET_NULL,
                               null=True, blank=True,
                               related_name="video2slot")

    def __str__(self):
        if self.is_active:
            status = "live"
        else:
            status = "inactive"
        return f" {self.name} -{status}"



