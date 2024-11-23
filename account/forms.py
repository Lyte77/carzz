from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'First Name'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Last Name'
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'placeholder':'Email'
        }
    ))
    is_dealer = forms.BooleanField(required=False,widget=forms.CheckboxInput(
        attrs={
        
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Password'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Confirm Password'
        }
    ))
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','email','password1','password2','is_dealer']


class LoginForm(AuthenticationForm):
     username = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder':'Email'
        }
    ))
     
     password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Password'
        }
    ))