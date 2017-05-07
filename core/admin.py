from django.contrib import admin
from django.contrib.admin import AdminSite
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.db import IntegrityError

from .models import Plover, Observation, Observer, Location
from .forms import ImportPloversForm
from extras.formatter import format_date, format_time, format_color

import csv
import os

DEFAULT_PAGINATION = 25


class MyAdminSite(AdminSite):
    def get_urls(self):
        from django.conf.urls import url
        urls = super(MyAdminSite, self).get_urls()
        urls += [
            url(r'^import-plovers/$', self.admin_view(self.import_plovers),
                name='import_plovers')
        ]
        return urls

    def save_location(self, town, department, locality):
        department = 'Calvados' if (department == '14') else 'Manche'
        location, location_exist = Location.objects.get_or_create(
            country='France',
            town=town.title(),
            department=department,
            locality=locality.title()
        )

        return location

    def save_bander(self, first_name, last_name):
        observer, observer_exist = Observer.objects.get_or_create(
            last_name=last_name,
            first_name=first_name,
            is_bander=True
        )

        return observer

    def save_bird(self, bird, bander, location):
        date = format_date(bird['banding_date'])
        time = format_time(bird['banding_time'])

        bird, bird_exist = Plover.objects.get_or_create(
            bander=bander,
            location=location,
            banding_year=bird['banding_year'],
            metal_ring=bird['metal_ring'],
            code=bird['code'],
            color=bird['color'],
            sex=bird['sex'],
            age=bird['age'],
            banding_date=date,
            banding_time=time
        )

        return bird, bird_exist

    def import_plovers_from_csv(self, uploaded_file):
        path = 'media/upload/'

        # If the upload folder doesn't exist, we create it
        if not os.path.exists(path):
            os.mkdir(path)

        # Save the uploaded file to
        with open(path + str(uploaded_file), 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
                print(destination)

        filepath = path + str(uploaded_file)
        cr = csv.DictReader(open(filepath, 'r', encoding='utf-8'))
        saved_plovers = {
            'recorded': [],
            'already_saved': [],
            'rejected': []
        }

        for row in cr:
            code = int(row['number'])
            color = row['color']

            if (code != 0 and color is not None):
                bird = {
                    'banding_year': row['banding_year'],
                    'metal_ring': row['metal_ring'],
                    'code': code,
                    'color': format_color(color),
                    'sex': row['sex'],
                    'age': row['age'],
                    'banding_date': row['date'],
                    'banding_time': row['banding_time']
                }
                location = self.save_location(
                    row['town'], row['department'], row['locality'])
                bander = self.save_bander(
                    row['first_name_observer'], row['observer'])

                try:
                    bird, bird_exist = self.save_bird(bird, bander, location)
                except IntegrityError as e:
                    saved_plovers['rejected'].append(bird)
                    print('Error : {}'.format(e))
                else:
                    if(bird_exist):
                        saved_plovers['recorded'].append(bird)
                        print('{} saved !'.format(bird))
                    else:
                        saved_plovers['already_saved'].append(bird)
                        print('{} already saved !'.format(bird))

        return saved_plovers

    # This section is coded only to migrate old data to this project
    def import_plovers(self, request):
        data = {}

        if request.method == 'POST':
            form = ImportPloversForm(request.POST, request.FILES)
            data['form'] = form
            if form.is_valid():
                data = self.import_plovers_from_csv(request.FILES['file'])

        else:
            data['form'] = ImportPloversForm()

        return render(request, 'admin/import.html', data)


class PloverAdmin(admin.ModelAdmin):
    list_display = ('id', 'metal_ring', 'code', 'color', 'sex', 'age')
    search_fields = ('code', 'color', 'metal_ring')
    list_filter = ('code', 'color')
    ordering = ('id',)
    list_per_page = DEFAULT_PAGINATION


class ObservationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'date', 'observer', 'plover', 'location', 'supposed_sex',
        'coordinate_x', 'coordinate_y', 'comment')
    search_fields = ('observer', 'plover', 'date', 'location')
    list_filter = ('plover',)
    ordering = ('-date',)
    list_per_page = DEFAULT_PAGINATION


class ObserverAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name')
    list_filter = ('last_name', 'first_name')
    search_fields = ('last_name', 'first_name')
    list_filter = ('last_name', 'first_name')
    ordering = ('id',)
    list_per_page = DEFAULT_PAGINATION


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'town', 'department', 'locality')
    list_filter = ('country', 'town', 'department')
    search_fields = ('country', 'town', 'department')
    list_filter = ('country', 'town', 'department')
    ordering = ('id',)
    list_per_page = DEFAULT_PAGINATION


admin.site = MyAdminSite()
admin.site.site_header = _('Administration')
admin.site.site_title = _('Banding tracking')

admin.site.register(Plover, PloverAdmin)
admin.site.register(Observation, ObservationAdmin)
admin.site.register(Observer, ObserverAdmin)
admin.site.register(Location, LocationAdmin)
