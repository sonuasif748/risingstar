from django import forms
from django.core import validators
from .models import Movies as Movies_Model
from .models import *
from django.contrib.auth.models import User
from user.models import *

class admincustomerform(forms.ModelForm):
    class Meta:
        model=customer
        fields='__all__'


class add_movie_form(forms.ModelForm):
    class Meta:
        model = Movies_Model
        fields = '__all__'



class add_tollywood_movie(forms.ModelForm):
    class Meta:
        model = Tollywood_Movie
        fields = '__all__'


class add_bollywood_movie(forms.ModelForm):
    class Meta:
        model = Bollywood_Movie
        fields = '__all__'


class add_hollywood_movie(forms.ModelForm):
    class Meta:
        model = Hollywood_Movie
        fields = '__all__'



# # Publisher
# class publisher_form(forms.ModelForm):
#     class Meta:
#         model = publisher
#         fields = ['username','password','email','company_name']
