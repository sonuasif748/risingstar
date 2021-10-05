from django.urls import path,include
from user.views import *

urlpatterns = [
    path('register/',register,name='register'),
    path('login/',loginuser,name='login'),
    path('logout/',logoutuser,name='logout'),
    path('test/',test,name='test'),
]