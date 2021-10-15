from django.contrib import admin
from django.urls import path,include
from homepage.views import *


urlpatterns = [
    path('home/',homepage, name='homepage'),
    path('allmovies/',allmovies, name='allmovies'),
    path('homeshows/',homeshows, name='homeshows'),
    path('homekids/',homekids, name='homekids'),
    path('homeaction/',homeaction, name='homeaction'),
    path('search/',search,name='search'),
    path('moviedetail-<str:title>/',moviedetail,name='moviedetail'),
    path('<str:pk>_movies/',viewallpage,name='language'),
    path('<str:pk>_movies/',viewallpage,name='geners'),
]