from django.shortcuts import render, redirect, get_object_or_404
from .forms import DealerProfileForm,DealerEditProfileForm

from .models import DealerProfileModel
# Create your views here.

def home_page(request):
    return render(request, 'carzz/home.html')

def profile_page(request, id):
    user = get_object_or_404(DealerProfileModel,user__id=id)
    print(user)
    
    context = {'user': user}
    return render(request, 'carzz/profile_page.html',context)


   

# def create_dealer_profile(request):
#     if request.method == 'POST':
#         form = DealerProfileForm(request.POST,request.FILES)
#         if form.is_valid():
#             user = request.user  # Access the currently logged-in user
#             form.instance.user = user
#             form.save()
#             print('profile sucessfully saved')
#             return redirect('carzz:profile')
#     else:
#         form =  DealerProfileForm(instance=request.user)
#     return render(request, 'carzz/profile_form.html',{'form':form})


def edit_profile(request):
    if request.method == 'POST':
        profile_form = DealerProfileForm(
            instance = request.user,
            data=request.POST,
            files = request.FILES
        )
        if profile_form.is_valid():
            profile_form.save()
            return redirect('carzz:profile')

    else:
        profile_form = DealerProfileForm(instance=request.user )
    return render(request, 'carzz/profile_form.html',{'profile_form':profile_form})