from django.contrib import admin
from django.http import HttpRequest
from .models import Category, Blog, aboutus, Social_link

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)

#to only create one about us data we will remove add button
class aboutusAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = aboutus.objects.all().count()
        if count == 0:
            return True
        return False
    
admin.site.register(aboutus, aboutusAdmin)

admin.site.register(Social_link)