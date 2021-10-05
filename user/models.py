from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class customer(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='static/images', null=True, blank=True)
    mobile = models.CharField(max_length=20, null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,
                              default='Male')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name