def search_formatter(plover_collector, form_class, form_url, request):
    data = {
        'form_url': form_url,
        'not_found': False
    }

    if request.method == 'POST':
        form = form_class(request.POST)

        if form.is_valid():
            plover = plover_collector()

            if plover:
                data['plover'] = plover
            else:
                data['not_found'] = True
    else:
        form = form_class()

    data['form'] = form

    return data
