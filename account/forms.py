from django import forms
from .models import CustomUser

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={ 
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm  focus:outline-red  focus:bg-white mt-5',
            'placeholder':'First Name'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm  focus:outline-none  focus:bg-white mt-5',
            'placeholder':'Last Name'
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm focus:outline-none  focus:bg-white mt-5',
            'placeholder':'Email'
        }
    ))
    is_dealer = forms.BooleanField(required=False,widget=forms.CheckboxInput(
        attrs={
            'class':'checked:border-red-500 h-3 w-[50px]',
        
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700 outline-none text-sm focus:outline-none  focus:bg-white mt-5',
            'placeholder':'Password'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm focus:outline-none  focus:bg-white mt-5',
            'placeholder':'Confirm Password'
        }
    ))
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','email','password1','password2','is_dealer']


class LoginForm(AuthenticationForm):
     username = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'w-full px-8 py-4 mb-5 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm   focus:bg-white',
            'placeholder':'Email'
        }
    ))
     
     password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white',
            'placeholder':'Password'
        }
    ))
     

