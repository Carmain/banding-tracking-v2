from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^administration$', views.administration, name='administration'),
    url(r'^map$', views.map, name='map'),
    url(r'^observations$', views.observations, name='observations'),
    url(r'^remove-plover/(?P<uuid>\w+)$', views.remove_plover,
        name='remove_plover'),
    url(r'^validation$', views.validate_plovers, name='validate_plovers'),

    url(r'^get-history/pattern/(?P<number>\d+)/(?P<color>\d+)$',
        views.get_history_by_code, name='get_history_by_code'),

    url(r'^get-history/ring/(?P<ring>\w+)$', views.get_history_by_metal_ring,
        name='get_history_by_metal_ring'),
]
