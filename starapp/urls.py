from django.contrib import admin
from django.urls import path,include
from starapp.views import *


urlpatterns = [
    path('',home,name='hompage'),
    path('movies/',movies,name='movies'),
    path('shows/',shows,name='shows'),
    path('kids/',kids,name='kids'),
    path('action/',action,name='action'),
    path('contact/',contact,name='contact'),
    path('searchbar/',search,name='search'),

]