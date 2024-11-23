from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from carzz.models import DealerProfileModel

# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            if user.is_dealer:
                dealer_profile = DealerProfileModel(user=user)
                dealer_profile.save()
           
            login(request,user) 
            messages.success(request, 'Account created sucessfully') 
            return redirect('carzz:home')

    else:
        form = CustomUserCreationForm()
    return render(request,'account/register.html',{'form':form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request,request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,email=email,password=password)

            if user is not None:
                login(request, user)
                return redirect('carzz:home')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})


def logout_user(request):
    logout(request)
    return redirect('login')