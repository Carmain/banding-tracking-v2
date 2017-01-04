from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def administration(request):
    return render(request, 'core/administration.html')


def observation_form(request):
    return render(request, 'core/observation_form.html')
