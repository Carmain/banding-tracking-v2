from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('search/metal', views.search_by_metal, name='search_by_metal'),
    path('search/code', views.search_by_code, name='search_by_code'),
    path('map', views.map, name='map'),
]
