from .models import Category
from .models import Social_link

def get_category(request):
    categories = Category.objects.all()
    return dict(categories = categories)

def get_social_link(request):
    social_link = Social_link.objects.all()
    return dict(social_link = social_link)