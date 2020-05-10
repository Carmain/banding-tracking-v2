from django.shortcuts import render
from website.utils.search_formatter import search_formatter
from website.models import Plover
from website.forms import CodeForm, MetalForm


def index(request):
    return render(request, 'website/home.html')


def about(request):
    return render(request, 'website/about.html')


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

    return render(request, 'website/search.html', data)


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

    return render(request, 'website/search.html', data)
