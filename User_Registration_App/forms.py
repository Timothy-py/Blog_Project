from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class user_reg_form(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ("username", 'email', 'password1', 'password2')

class user_update_form(forms.ModelForm):

    class Meta():
        model = User
        fields = ('username', 'email')

class profile_update_form(forms.ModelForm):

    class Meta():
        model = UserProfile
        fields = ('picture',)
