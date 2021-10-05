from django.db import models
from django.contrib.auth.models import User


class Movies(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)
    discription = models.CharField(max_length=10000, null=True, blank=True)
    image = models.ImageField(upload_to="static/images", null=True, blank=True)
    screen_shot = models.ImageField(upload_to='static/images', null=True, blank=True)
    movie_length = models.CharField(max_length=50, null=True, blank=True)
    movie_director = models.CharField(max_length=200, null=True, blank=True)
    movie_actor = models.CharField(max_length=1000, null=True, blank=True)
    movie_link = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.name

    def snippet(self):
        return self.discription[:10]+'...'


class Tollywood_Movie(Movies):
    lang = models.CharField(max_length=500)
    def __str__(self):
        return self.name


class Bollywood_Movie(Movies):
    lang = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Hollywood_Movie(Movies):
    lang = models.CharField(max_length=500)
    def __str__(self):
        return self.name

