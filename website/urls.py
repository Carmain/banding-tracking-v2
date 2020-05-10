from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('search/metal', views.search_by_metal, name='search_by_metal'),
    path('search/code', views.search_by_code, name='search_by_code'),
    path('map', views.map, name='map'),
    path('observations', views.observations, name='observations'),
    path(r'^remove-plover/(?P<uuid>\w+)$', views.remove_bird_in_session,
         name='remove_bird_in_session'),
    path('validation', views.validate_plovers, name='validate_plovers'),
]
