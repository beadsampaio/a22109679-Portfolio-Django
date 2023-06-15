from django.shortcuts import render
from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('users', views.users_page_view, name='users'),
    path('about', views.about_page_view, name='about'),
    path('interesses', views.interesses_page_view, name='interesses'),
    path('education', views.education_page_view, name='education'),
    path('projects', views.projects_page_view, name='projects'),
    path('contact', views.contact_page_view, name='contact'),
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),
    path('cadeiraForm', views.cadeira_form_page_view, name='cadeiraForm'),
    path('projetoForm', views.projeto_form_page_view, name='projetoForm'),
    path('tfcForm', views.tfc_form_page_view, name='tfcForm'),


]
