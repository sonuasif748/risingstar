from django import forms
from .models import *

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput()
        }
class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ['mobile', 'profile_pic', 'gender']
        GENDER_CHOICES = (
            ('Male', 'Male'),
            ('Female', 'Female'),
        )