from django import forms
from django.contrib.auth.forms import UserCreationForm
from twitteruser.models import MyUser

class SignupForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 
                  'displayname',
                )