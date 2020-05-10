from django.shortcuts import render
from website.utils.views_sinppets import get_or_none, search_formatter
from website.models import Plover
from website.forms import CodeForm, MetalForm


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
