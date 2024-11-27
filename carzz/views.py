from django.shortcuts import render, redirect, get_object_or_404
from .forms import DealerProfileForm,DealerEditProfileForm
from django.core.exceptions import ValidationError
from account.models import CustomUser

from .models import DealerProfileModel
# Create your views here.

def home_page(request):
    return render(request, 'carzz/home.html')


def profile_page(request):
    profiles = DealerProfileModel.objects.exclude(user=request.user)

    return render(request, 'carzz/profile_page.html', {'profiles':profiles})

def profile(request,pk):
    if request.user.is_authenticated:
        
        profile = DealerProfileModel.objects.get(user_id=pk)
        user = request.user
        check_profile  = DealerProfileModel.objects.filter(user=user).first()
        return render(request, 'carzz/profile.html',{'profile':profile,
                                                     'has_profile': bool(check_profile),})
    else:
        return redirect('carzz:home')

   
def setup_profile(request):
    if request.user.is_authenticated:
        if request.user.is_dealer:
            if request.method == 'POST':
                profile_form = DealerProfileForm(request.POST,request.FILES)
                if profile_form.is_valid():
                    user = request.user
                    profile = profile_form.save(commit=False)
                    profile.user = user  
                    
                    profile.save()
                    return redirect('carzz:profile',request.user.id )
            else:
            
                profile_form = DealerProfileForm()
            return render(request, 'carzz/profile_form.html',
                          {'profile_form':profile_form})


   
            
def update_profile(request):
    if request.user.is_authenticated:
        current_profile = DealerProfileModel.objects.get(user=request.user)
        profile_form = DealerProfileForm(request.POST or None, instance=current_profile)
        if  profile_form.is_valid():
            profile_form.save()
            return redirect('carzz:profile',request.user.id )
    return render(request, 'carzz/profile_form.html',{'profile_form':profile_form})
   
