from django.shortcuts import render, redirect, get_object_or_404
from blog_app.models import Category, Blog, aboutus
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, BlogPostForm
from django.template.defaultfilters import slugify

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    context = {
        'category_count' : category_count,
        'blogs_count' : blogs_count,

    }
    return render(request, "Dashboard/dashboard.html", context)

def categories(request):
    return render(request, "Dashboard/categories.html")

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        "form" : form
    }
    return render(request, "Dashboard/addcategory.html", context)

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid:
            form.save()
            return redirect("categories")

    form = CategoryForm(instance=category)
    context = {
        "form" : form,
        "category" : category,
    }
    return render(request, "Dashboard/edit_category.html", context)

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

def posts(request):
    posts = Blog.objects.all()
    context = {
        "posts" : posts,
    }
    return render(request, "Dashboard/posts.html", context)

def add_posts(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user # temporarily saving the form
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('posts')
        else:
            print('form is invalid')
            print(form.errors)
    form = BlogPostForm()
    context = {
        "form" : form,
    }
    return render(request, "Dashboard/add_posts.html", context)

def edit_posts(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify('title') + '-'+str(post.id)
            post.save()
            return redirect('posts')

    form = BlogPostForm(instance=post)
    context = {
        "form" : form,
        "post" : post,
    }
    return render(request, "Dashboard/edit_posts.html", context)

def delete_posts(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')