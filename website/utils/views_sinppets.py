def get_or_none(class_model, **kwargs):
    try:
        return class_model.objects.get(**kwargs)
    except class_model.DoesNotExist:
        return None


def search_formatter(plover, form_class, form_url, request):
    data = {
        'form_url': form_url,
        'not_found': False
    }

    if request.method == 'POST':
        form = form_class(request.POST)

        if form.is_valid():
            if plover:
                data['plover'] = plover
            else:
                data['not_found'] = True
    else:
        form = form_class()

    data['form'] = form

    return data
