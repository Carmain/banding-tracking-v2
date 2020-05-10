from django.shortcuts import render
from website.utils.views_sinppets import (
    get_or_none, search_formatter, flush_session)
from website.models import Plover
from website.forms import CodeForm, MetalForm, MapForm
from django.http import HttpResponseRedirect


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

    return render(request, 'website/map.html', {'form': map_form})
