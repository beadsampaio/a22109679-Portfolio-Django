from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.urls import reverse

from .forms import *
from .models import *

from django.contrib.auth import authenticate, login, logout


def home_page_view(request):
    return render(request, 'portfolio/home.html')

def users_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))
    return render(request, 'portfolio/users.html')

def about_page_view(request):
    context = {
        'linguas': Lingua.objects.all(),
        'competencias': Competencia.objects.all(),
    }
    return render(request, 'portfolio/about.html', context)

def interesses_page_view(request):
    context = {
        'interesses': Interesse.objects.all(),
    }
    return render(request, 'portfolio/interesses.html', context)


def education_page_view(request):

    context = {
        'educations': Educacao.objects.all(),
        'cadeiras': Cadeira.objects.all(),
        'projetos': Projeto.objects.all(),
    }
    return render(request, 'portfolio/education.html', context)


def projects_page_view(request):
    context = {
        'projetos': Projeto.objects.all(),
        'tfcs': TFC.objects.all(),
    }
    return render(request, 'portfolio/projects.html', context)


def contact_page_view(request):
    context = {
        'laboratorios': Laboratorio.objects.all(),
        'tecnologiawebsites': Tecnologiawebsite.objects.all(),
    }
    return render(request, 'portfolio/contact.html', context)

def login_page_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:users'))
        else:
            return render(request, "portfolio/login.html", {'message:"Invalid credentials'})
    return render(request, 'portfolio/login.html')

def logout_page_view(request):
    logout(request)
    return render(request, 'portfolio/login.html', {
        'message': "Logged out.  "
    })

def cadeira_form_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))
    form = CadeiraForm()
    context = {'form': form}

    return render(request, 'portfolio/cadeiraForm.html', context)

def projeto_form_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))
    form = ProjetoForm()
    context = {'form': form}

    return render(request, 'portfolio/projetoForm.html', context)


def tfc_form_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))
    form = TfcForm()
    context = {'form': form}

    return render(request, 'portfolio/tfcForm.html', context)


