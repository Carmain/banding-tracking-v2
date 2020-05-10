import os

from django.shortcuts import render
from django.urls import reverse
from website.utils.views_sinppets import (
    get_or_none, search_formatter, flush_session, add_plover_in_session)
from website.models import Plover, Location, Observer, Observation
from website.forms import CodeForm, MetalForm, MapForm, PloverForm
from django.http import HttpResponseRedirect
from uuid import uuid4


def index(request):
    return render(request, 'website/home.html')


def about(request):
    return render(request, 'website/about.html')


def search_by_code(request):
    plover = get_or_none(
        Plover, code=request.POST.get('code'), color=request.POST.get('color'))
    data = search_formatter(plover, CodeForm, 'search_by_code', request)

    return render(request, 'website/search.html', data)


def search_by_metal(request):
    plover = get_or_none(Plover, metal_ring=request.POST.get('metal_ring'))
    data = search_formatter(plover, MetalForm, 'search_by_metal', request)

    return render(request, 'website/search.html', data)


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
                'email': request.POST.get('email'),
                'town': request.POST.get('town'),
                'department': request.POST.get('department'),
                'country': request.POST.get('country'),
                'locality': request.POST.get('locality'),
                'coordinate_x': request.POST.get('coordinate_x'),
                'coordinate_y': request.POST.get('coordinate_y')
            }

            return HttpResponseRedirect('/observations')
    else:
        map_form = MapForm()

    return render(request, 'website/map.html', {
        'form': map_form,
        'google_map_api_key': os.getenv("GOOGLE_MAP_API_KEY")
    })


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
                    'uuid': uuid4().hex,
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
        return render(request, 'website/observations.html', data)
    else:
        return HttpResponseRedirect(reverse('map'))


def remove_bird_in_session(request, uuid):
    bird_in_session = request.session.get('plovers')
    bird = [el for el in bird_in_session if el.get('uuid') != uuid]
    request.session['plovers'] = bird

    return HttpResponseRedirect(reverse('observations'))


def validate_plovers(request):
    def parse_form_coords(coord):
        coord = coord.strip()
        return float(coord) if coord else 0

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
        first_name=general.get('first_name'),
        email=general.get('email')
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
                coordinate_x=parse_form_coords(general.get('coordinate_x')),
                coordinate_y=parse_form_coords(general.get('coordinate_y'))
            )

            accepted_observations.append(plover)
        else:
            rejected_observations.append(observation)

    result = {
        'location': location,
        'accepted_observations': accepted_observations,
        'rejected_observations': rejected_observations
    }

    return render(request, 'website/result.html', result)
