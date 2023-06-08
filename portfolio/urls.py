from django.shortcuts import render
from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('about', views.about_page_view, name='about'),
    path('projects', views.projects_page_view, name='projects'),
    path('contact', views.contact_page_view, name='contact')


]
