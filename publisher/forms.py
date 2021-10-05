from django import forms
from .models import *
GENDER_CHOICES = (
            ('Male', 'Male'),
            ('Female', 'Female'),
        )
class PublisherUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput()
        }
class PublisherForm(forms.ModelForm):
    class Meta:
        model = publisher
        fields = ['company_name','mobile', 'profile_pic', 'gender']
        GENDER_CHOICES = (
            ('Male', 'Male'),
            ('Female', 'Female'),
        )


category_choice=[('Movie','Movie'),('Show','Show'),('Webseries','Webseries'),('Kids','Kids')]
language_choice=[('Telugu','Telugu'),('Hindi','Hindi'),('Tamil','Tamil'),
                 ('Malayalam','Malayalam'),('Kannada','Kannada'),('English','English')]
geners_choice = [('Action', 'Action'), ('Adventure', 'Adventure'), ('Comedy', 'Comedy'),
                 ('Horror', 'Horror'),('Thirller', 'Thirller'),('Drama', 'Drama'),
                 ('Romance', 'Romance'),('Sci Fi', 'Sci Fi')]
status_choice= [('Pending','Pending'),('Approve','Approve')]

class pub_add_movie_form(forms.ModelForm):
    class Meta:
        model = add_categories
        fields = ('publisher_name','category','title','discription','image','language','geners','screen_shot','movie_length','movie_director','actor_name','movie_link')



class pub_admin_movie_form(forms.ModelForm):
    class Meta:
        model = add_categories
        fields = ('publisher_name','category','title','discription','image','language','geners','screen_shot','movie_length','movie_director','actor_name','movie_link')

class pub_admin_changestatus(forms.ModelForm):
    class Meta:
        model = add_categories
        fields = ['status']