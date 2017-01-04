from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^administration$', views.administration, name='administration'),
    url(r'^new-observation$', views.observation_form, name='observation_form'),
]
