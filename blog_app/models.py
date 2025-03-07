from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name

STATUS_CHOICES = (
    ("Draft", "Draft"),
    ("Published", "Published"),
)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    author = models.ForeignKey(User , on_delete = models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(choices=STATUS_CHOICES,max_length=10, default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class aboutus(models.Model):
    about_us = models.TextField(max_length=500)
    
    class Meta:
        verbose_name_plural = 'about_us'

class Social_link(models.Model):
    platform = models.CharField(max_length=30)
    link = models.URLField(max_length=100)

    def __str__(self):
        return self.platform
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.comment