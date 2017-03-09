import uuid

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from core.models import Location, Observer, Observation, Plover

from .forms import MapForm, PloverForm, CodeForm, MetalForm
from .views_snippets import *


def index(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


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


def observations(request):
    if request.session.get('general', False):
        data = {
            'general': request.session.get('general')
        }

        if request.method == 'POST':
            plover_form = PloverForm(request.POST)

            if plover_form.is_valid():
                form_data = plover_form.cleaned_data

                plover = {
                    'uuid': uuid.uuid4().hex,
                    'code': form_data['code'],
                    'color': form_data['color'],
                    'sex': form_data['sex'],
                    'comment': form_data['comment']
                }

                add_plover_in_session(request, plover)
                data['plovers'] = request.session.get('plovers')

        elif request.session.get('plovers', False):
            data['plovers'] = request.session.get('plovers')
            plover_form = PloverForm()

        else:
            plover_form = PloverForm()

        data['form'] = plover_form
        return render(request, 'core/observations.html', data)
    else:
        return HttpResponseRedirect(reverse('map'))


def remove_plover(request, uuid):
    plovers_in_session = request.session.get('plovers')
    plovers = [el for el in plovers_in_session if el.get('uuid') != uuid]
    request.session['plovers'] = plovers

    return HttpResponseRedirect(reverse('observations'))


def validate_plovers(request):
    general = request.session.get('general')
    observations = request.session.get('plovers')
    accepted_observations = []
    rejected_observations = []

    location, location_exist = Location.objects.get_or_create(
        country=general.get('country'),
        town=general.get('town'),
        department=general.get('department'),
        locality=general.get('locality')
    )

    observer, observer_exist = Observer.objects.get_or_create(
        last_name=general.get('last_name'),
        first_name=general.get('first_name')
    )

    for observation in observations:
        try:
            plover = Plover.objects.get(
                code=observation.get('code'),
                color=observation.get('color')
            )
        except Plover.DoesNotExist:
            plover = None

        if plover:
            observation_saved, created = Observation.objects.get_or_create(
                observer=observer,
                location=location,
                plover=plover,
                date=general.get('date'),
                supposed_sex=observation.get('sex'),
                comment=observation.get('comment'),
                coordinate_x=general.get('coordinate_x'),
                coordinate_y=general.get('coordinate_y')
            )

            accepted_observations.append(plover)
        else:
            rejected_observations.append(observation)

    result = {
        'location': location,
        'accepted_observations': accepted_observations,
        'rejected_observations': rejected_observations
    }
    return render(request, 'core/result.html', result)


def search_by_code(request):
    def collector():
        try:
            plover = Plover.objects.get(
                code=request.POST.get('code'),
                color=request.POST.get('color')
            )
        except Plover.DoesNotExist:
            plover = None

        return plover

    data = search_formatter(collector, CodeForm, 'search_by_code', request)

    return render(request, 'core/search.html', data)


def search_by_metal(request):
    def collector():
        try:
            plover = Plover.objects.get(
                metal_ring=request.POST.get('metal_ring'),
            )
        except Plover.DoesNotExist:
            plover = None

        return plover

    data = search_formatter(collector, MetalForm, 'search_by_metal', request)

    return render(request, 'core/search.html', data)
