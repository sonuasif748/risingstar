from django.contrib import admin
from django.urls import path,include
from admin_dashboard.views import *


urlpatterns = [
    # Admin Urls

    path('dashboardlogin/', dashboardlogin, name='dashboardlogin'),
    path('dashlogout/', dashlogout, name='dashlogout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add_movies/', add_movie, name='add_movie'),
    path('add_tm/', add_tm, name='add_tm'),
    path('add_bm/', add_bm, name='add_bm'),
    path('add_hm/', add_hm, name='add_hm'),
    path('movieslist/', movieslist, name='movieslist'),

    path('library/', library, name='library'),

    path('usersmodify/', usersmodify, name='usersmodify'),
    path('createuser/',createuser,name='createuser'),
    path('deleteuser/<int:id>/',delete_user,name='delete_user'),
    path('updateuser<int:id>/',update_user,name='update_user'),

    path('delete/<int:id>/', delete_movie, name='delete'),
    path('update<int:id>/', update_movie, name='update'),

    path('published_movies/', published_movies, name='published_movies'),
    path('pub_update_movie-<int:id>/', pub_update_movie, name='pub_update_movie'),
    path('admin_pub_status_update-<int:id>/', admin_pub_status_update, name='admin_pub_status_update'),
    path('pub_delete_movie/<int:id>/', pub_delete_movie, name='pub_delete_movie'),

    path('update_status/<int:status>/<int:id>',update_status,name='update_status'),
]