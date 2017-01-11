from django.shortcuts import render
from django.template.loader import render_to_string
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
        location = {
            'date': request.POST.get('date'),
            'town': request.POST.get('town'),
            'department': request.POST.get('department'),
            'country': request.POST.get('country'),
            'location': request.POST.get('location'),
            'coordinate_x': request.POST.get('coordinate_x'),
            'coordinate_y': request.POST.get('coordinate_y')
        }

        return render(request, 'core/observations.html', location)
    else:
        # redirect to a new URL:
        return HttpResponseRedirect('map')
