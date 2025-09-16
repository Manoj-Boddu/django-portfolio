from django.shortcuts import render
from .models import Project, BlogPost  # 👈 only use BlogPost for your blog

# Home page
def home(request):
    return render(request, 'internalHome/home.html')

# About page
def about(request):
    return render(request, 'internalHome/about.html')

# Contact page
def contact(request):
    return render(request, 'internalHome/contact.html')

# Projects page (from database)
def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'internalHome/projects.html', {'projects': all_projects})

# Blog page (dynamic)
def blog(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'internalHome/blog.html', {'posts': posts})
