from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^map$', views.map, name='map'),
    url(r'^observations$', views.observations, name='observations'),
    url(r'^remove-plover/(?P<uuid>\w+)$', views.remove_bird_in_session,
        name='remove_bird_in_session'),
    url(r'^validation$', views.validate_plovers, name='validate_plovers'),
    url(r'^search/metal$', views.search_by_metal, name='search_by_metal'),
    url(r'^search/code$', views.search_by_code, name='search_by_code'),
    url(r'^export-to-pdf/(?P<metal_ring>\w+)$', views.get_report,
        name='get_report'),
]
