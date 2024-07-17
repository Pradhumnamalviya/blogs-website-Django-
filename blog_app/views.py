from django.shortcuts import render
from .models import Category, Blog
from django.shortcuts import render , redirect, get_object_or_404

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status  = 'Published', category = category_id)

    try:
        category = Category.objects.get(pk = category_id)
    except:
        return redirect('404.html')
    
    # category = get_object_or_404(Category, pk = category_id)
    
    context = {
        "posts" : posts,
        "category" : category
    }
    
    return render(request, "posts_by_category.html", context)

