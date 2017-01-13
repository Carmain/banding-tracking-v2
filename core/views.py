import uuid

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

    if request.method == 'POST':
        request.session['location'] = {
            'date': request.POST.get('date'),
            'town': request.POST.get('town'),
            'department': request.POST.get('department'),
            'country': request.POST.get('country'),
            'location': request.POST.get('location'),
            'coordinate_x': request.POST.get('coordinate_x'),
            'coordinate_y': request.POST.get('coordinate_y')
        }

        return HttpResponseRedirect('/observations')
    else:
        return render(request, 'core/map.html')


# Not a view
def add_plover_in_session(request, plover):
    if 'plovers' not in request.session or not request.session['plovers']:
        request.session['plovers'] = [plover]
    else:
        plovers_list = request.session['plovers']
        plovers_list.append(plover)
        request.session['plovers'] = plovers_list


def observations(request):
    if request.session.get('location'):
        data = {
            'location': request.session.get('location')
        }

        if request.method == 'POST':
            plover = {
                'uuid': uuid.uuid4().hex,
                'code': request.POST.get('code'),
                'color': request.POST.get('color'),
                'sex': request.POST.get('sex'),
                'comment': request.POST.get('comment')
            }

            add_plover_in_session(request, plover)
            data['plovers'] = request.session.get('plovers')

        elif request.session.get('plovers'):
            data['plovers'] = request.session.get('plovers')

        return render(request, 'core/observations.html', data)
    else:
        return HttpResponseRedirect('/map')


def remove_plover(request, uuid):
    plovers_in_session = request.session.get('plovers')
    plovers = [el for el in plovers_in_session if el.get('uuid') != uuid]
    request.session['plovers'] = plovers

    return HttpResponseRedirect('/observations')
