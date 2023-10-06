from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import RegularUser


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = RegularUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]      
    

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

