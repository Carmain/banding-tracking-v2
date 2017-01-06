from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def administration(request):
    return render(request, 'core/administration.html')


def map(request):
    return render(request, 'core/map.html')


def observations(request):
    return render(request, 'core/observations.html')
