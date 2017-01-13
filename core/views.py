from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def administration(request):
    return render(request, 'core/administration.html')


def map(request):
    # TODO: Check if it's a good ID...
    request.session.flush()
    return render(request, 'core/map.html')


def observations(request):
    data = {}

    if not request.session.get('location'):
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

            request.session['location'] = location
            data['location'] = location

            return render(request, 'core/observations.html', data)
    else:
        if request.method == 'POST':
            plover = {
                'code': request.POST.get('code'),
                'color': request.POST.get('color'),
                'sex': request.POST.get('sex'),
                'comment': request.POST.get('comment')
            }

            if 'plovers' not in request.session or not request.session['plovers']:
                request.session['plovers'] = [plover]
            else:
                plovers_list = request.session['plovers']
                plovers_list.append(plover)
                request.session['plovers'] = plovers_list

            data['location'] = request.session.get('location')
            data['plovers'] = request.session.get('plovers')

            return render(request, 'core/observations.html', data)
        else:
            # redirect to a new URL:
            return HttpResponseRedirect('map')
