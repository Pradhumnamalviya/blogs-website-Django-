from django.shortcuts import render, redirect
from blog_app.models import Category, Blog, aboutus
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import auth

def home(request):
    featured_blog = Blog.objects.filter(is_featured = True).order_by('updated_at')
    recent_blog = Blog.objects.filter(is_featured = False).order_by('updated_at')
    about = aboutus.objects.all()
    context = {
       "featured_blog" : featured_blog,
       "recent_blog" : recent_blog,
       "about" : about
    }
    return render(request, "home.html", context) 
 
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:   
         form = RegistrationForm()
    context = {
        "form" : form
    }
    return render(request, "register.html", context)

def login(request):
   if request.method == 'POST':
       form = AuthenticationForm(request, request.POST)
       if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
        return redirect('home')
    
   form = AuthenticationForm()
   context = {
        "form" : form
    }
   return render(request, "login.html", context)

def logout(request):
    auth.logout(request)
    return redirect('home')

