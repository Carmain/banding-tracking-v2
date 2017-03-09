from django.contrib import admin
from .models import Plover, Observation, Observer, Location

PAGINATION = 25


class PloverAdmin(admin.ModelAdmin):
    list_display = ('id', 'metal_ring', 'code', 'color', 'sex', 'age')
    search_fields = ('code', 'color', 'metal_ring')
    list_filter = ('code', 'color')
    ordering = ('id',)
    list_per_page = PAGINATION


class ObservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'observer', 'plover', 'location',
                    'supposed_sex', 'coordinate_x', 'coordinate_y', 'comment')
    search_fields = ('observer', 'plover', 'date', 'location')
    list_filter = ('plover',)
    ordering = ('-date',)
    list_per_page = PAGINATION


class ObserverAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name')
    list_filter = ('last_name', 'first_name')
    search_fields = ('last_name', 'first_name')
    list_filter = ('last_name', 'first_name')
    ordering = ('id',)
    list_per_page = PAGINATION


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'town', 'department', 'locality')
    list_filter = ('country', 'town', 'department')
    search_fields = ('country', 'town', 'department')
    list_filter = ('country', 'town', 'department')
    ordering = ('id',)
    list_per_page = PAGINATION

admin.site.register(Plover, PloverAdmin)
admin.site.register(Observation, ObservationAdmin)
admin.site.register(Observer, ObserverAdmin)
admin.site.register(Location, LocationAdmin)
