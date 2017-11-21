from django.contrib.auth.models import User
from django.forms import ModelForm,PasswordInput
from .models import *
import forms

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password','first_name','last_name')


