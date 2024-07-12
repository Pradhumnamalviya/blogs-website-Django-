from django.shortcuts import render
# from todoapp.models import Task

def home(request):
    return render(request, "home.html") 