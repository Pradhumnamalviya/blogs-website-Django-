from django.shortcuts import render
from blog_app.models import Category, Blog

def home(request):
    featured_blog = Blog.objects.filter(is_featured = True).order_by('updated_at')
    recent_blog = Blog.objects.filter(is_featured = False).order_by('updated_at')
    context = {
       "featured_blog" : featured_blog,
       "recent_blog" : recent_blog
    }
    return render(request, "home.html", context) 