from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfileTable

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileTable
        fields = ['name','email','service']
