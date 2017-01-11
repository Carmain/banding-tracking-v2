from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def administration(request):
    return render(request, 'core/administration.html')


def map(request):
    return render(request, 'core/map.html')


def observations(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        return render(request, 'core/observations.html')
    else:
        # redirect to a new URL:
        return HttpResponseRedirect('map')
