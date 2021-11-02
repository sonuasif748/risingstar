from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

# Publishers Models

class publisher(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='static/images', null=True, blank=True)
    mobile = models.CharField(max_length=20, null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,
                              default='Male')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

category_choice=[('Movie','Movie'),('Show','Show'),('Webseries','Webseries'),('Kids','Kids')]
language_choice=[('Telugu','Telugu'),('Hindi','Hindi'),('Tamil','Tamil'),
                 ('Malayalam','Malayalam'),('Kannada','Kannada'),('English','English')]
geners_choice = [('Action', 'Action'), ('Adventure', 'Adventure'), ('Comedy', 'Comedy'),
                 ('Horror', 'Horror'),('Thirller', 'Thirller'),('Drama', 'Drama'),
                 ('Romance', 'Romance'),('Sci Fi', 'Sci Fi')]

class add_categories(models.Model):
    publisher_name=models.CharField(max_length=500)
    category=models.CharField(max_length=500,choices=category_choice)
    title=models.CharField(max_length=500)
    discription = models.CharField(max_length=10000, null=True, blank=True)
    image = models.ImageField(upload_to="static/images", null=True, blank=True)
    language=models.CharField(max_length=500,choices=language_choice)
    geners=models.CharField(max_length=500,choices=geners_choice)
    screen_shot = models.ImageField(upload_to='static/images', null=True, blank=True)
    movie_length = models.CharField(max_length=50, null=True, blank=True)
    movie_director = models.CharField(max_length=200, null=True, blank=True)
    actor_name = models.CharField(max_length=1000, null=True, blank=True)
    movie_link = models.CharField(max_length=10000, null=True, blank=True)
    status=models.BooleanField(default=0)

    def __str__(self):
        return self.title