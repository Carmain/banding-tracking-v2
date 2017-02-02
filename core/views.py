import uuid

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import MapForm


def index(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def administration(request):
    return render(request, 'core/administration.html')


def flush_session(request, keys):
    for key in keys:
        if key in request.session:
            del request.session[key]


def map(request):
    flush_session(request, ('plovers', 'general'))

    if request.method == 'POST':
        map_form = MapForm(request.POST)
        # check whether it's valid:
        if map_form.is_valid():
            request.session['general'] = {
                'date': request.POST.get('date'),
                'last_name': request.POST.get('last_name').upper(),
                'first_name': request.POST.get('first_name').capitalize(),
                'town': request.POST.get('town'),
                'department': request.POST.get('department'),
                'country': request.POST.get('country'),
                'location': request.POST.get('location'),
                'coordinate_x': request.POST.get('coordinate_x'),
                'coordinate_y': request.POST.get('coordinate_y')
            }

            return HttpResponseRedirect('/observations')
    else:
        map_form = MapForm()

    return render(request, 'core/map.html', {'form': map_form})


def add_plover_in_session(request, plover):
    if 'plovers' not in request.session or not request.session['plovers']:
        request.session['plovers'] = [plover]
    else:
        plovers_list = request.session['plovers']
        plovers_list.append(plover)
        request.session['plovers'] = plovers_list


def observations(request):
    if request.session.get('general'):
        data = {
            'general': request.session.get('general')
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
