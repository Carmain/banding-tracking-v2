def flush_session(request, keys):
    for key in keys:
        if key in request.session:
            del request.session[key]


def add_plover_in_session(request, plover):
    if 'plovers' not in request.session or not request.session['plovers']:
        request.session['plovers'] = [plover]
    else:
        plovers_list = request.session['plovers']

        if not any(bird['color'] == plover['color'] and
                   bird['code'] == plover['code'] for bird in plovers_list):
            plovers_list.append(plover)
            request.session['plovers'] = plovers_list


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
