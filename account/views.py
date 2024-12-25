from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import CustomUser
from carzz.models import DealerProfileModel
from carzz.forms import DealerProfileForm

# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        try:

            if form.is_valid():
                user = form.save()

            # if user.is_dealer:
            #     dealer_profile = DealerProfileModel(user=user)
            #     dealer_profile.save()
           
            login(request,user) 
            messages.success(request, 'Account created sucessfully') 
            return redirect('carzz:home')
        except ValueError as e:
            print(f'Error {e}')


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
                messages.success(request, "Login Successful")
                return redirect('carzz:home')
        else:
            print("Wrong creds")

    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})


def logout_user(request):
    logout(request)
    return redirect('login')

def update_user(request):
    if request.user.is_authenticated:
        current_user = CustomUser.objects.get(id=request.user.id)
        form = CustomUserCreationForm(request.POST or None, instance=current_user)
       
        if form.is_valid():
            form.save()
          
            login(request,current_user)
            print("updated")
            messages.success("User updated sucessfully")
            return redirect('carzz:home')
        return render(request,'account/update_user.html',{'form':form,
                                                          })
    else:
        messages.error(request,("You must log in to view page"))
        return redirect('login')
    
        
