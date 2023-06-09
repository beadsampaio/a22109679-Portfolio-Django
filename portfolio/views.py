from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def home_page_view(request):
    return render(request, 'portfolio/home.html')

def menu_page_view(request):
    return render(request, 'portfolio/menu.html')

def about_page_view(request):
    return render(request, 'portfolio/about.html')

def projects_page_view(request):
    return render(request, 'portfolio/projects.html')


def contact_page_view(request):
    return render(request, 'portfolio/contact.html')