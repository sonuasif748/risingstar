from django.urls import path, include
from publisher.views import *
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    # publishers urls

    path('publisher-register/',publisher_register,name='publisher-register'),
    path('publisher-login/',publisher_login,name='publisher-login'),
    path('publisher/',publisher,name='publisher'),
    path('pubadd_movies/', pub_add_movie, name='pub_add_movie'),
    path('pubadd_tm/', pub_add_tm, name='pub_add_tm'),
    path('pubadd_bm/', pub_add_bm, name='pub_add_bm'),
    path('pubadd_hm/', pub_add_hm, name='pub_add_hm'),
    path('pubmoviestatus/', moviesstatus, name='moviesstatus'),
    path('pubupdate_<int:id>/', pub_update_movie, name='pubupdatemovies'),
]