from django.shortcuts import render, redirect, get_object_or_404
from .forms import DealerProfileForm,DealerEditProfileForm
from django.core.exceptions import ValidationError
from account.models import CustomUser
from .forms import DealerAddCarForm, DealerAddImagesForm
from .models import Car, CarImage

from .models import DealerProfileModel
# Create your views here.

def home_page(request):
        cars = Car.objects.all()
        
        context = {'cars':cars,
                   }
       
        return render(request, 'carzz/home.html',context)
    
    

def car_detail_page(request,id):
    car = get_object_or_404(Car,id=id)
    
    context = {'car':car,
              
               }
    return render(request,'carzz/car_detail.html',context)



def dashboard(request, dealer_id):
    if request.user.is_authenticated:
        # dealer_cars = Car.objects.all()
        # if dealer_cars:
        #     print(dealer_cars)
        # else:
        #     print("You have no cars already")
        if request.user.is_dealer:
            dealer = request.user
            dealer_profile =  get_object_or_404(DealerProfileModel,user_id=dealer_id)
            dealer_cars = Car.objects.filter(dealer=dealer_profile)
            if dealer_cars:
                print(dealer_cars)
            else:
                print("No cars yet")
            return render(request, 'carzz/dashboard.html',{'dealer':dealer,
                                                           'dealer_profile':dealer_profile,
                                                           'dealer_cars':dealer_cars})

def dealer_profile(request,dealer_id):
   dealer_profile = get_object_or_404(DealerProfileModel,user_id=dealer_id)
  
   context = {'dealer_profile':dealer_profile,
             }
   return render(request,'carzz/dealer_profile.html',context)


def setup_profile(request):
    if request.user.is_authenticated and request.user.is_dealer:
        if request.method == 'POST':
            profile_form = DealerProfileForm(request.POST, request.FILES)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)  # Avoid unnecessary database write-through
                profile.user = request.user
                profile.save()
                return redirect('carzz:dealer_profile', request.user.id)
        else:
            profile_form = DealerProfileForm()
        return render(request, 'carzz/profile_form.html',{'profile_form':profile_form})
    else:
        
        return redirect('login')  


# def update_profile(request):
#     if request.user.is_authenticated:
#         current_profile = DealerProfileModel.objects.get(user=request.user)
#         profile_form = DealerProfileForm(request.POST or None,request.FILES, instance=current_profile)
#         if  profile_form.is_valid():
#             profile_form.save()
#             return redirect('carzz:dealer_profile',request.user.id )
        
#     return render(request, 'carzz/profile_form.html',{'profile_form':profile_form})


def update_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            current_profile = DealerProfileModel.objects.get(user=request.user)

            form = DealerEditProfileForm(data=request.POST,files=request.FILES,
                                     instance=current_profile)
            if form.is_valid():
                form.save()
                return redirect('carzz:dashboard', dealer_id=request.user.id)
        else:
            current_profile = DealerProfileModel.objects.get(user=request.user)
            form = DealerEditProfileForm(instance=current_profile)
        return render(request, 'carzz/profile_form.html',{'profile_form':form})


def add_car(request):
    if request.user.is_authenticated:
      if request.user.is_dealer:
          image_form = DealerAddImagesForm()
          if request.method == 'POST':
              car = Car(dealer=DealerProfileModel.objects.get(user=request.user))
             
              car.save()
            #   car_image_form = DealerAddImagesForm(request.POST,request.FILES,instance=car)
              form = DealerAddCarForm(request.POST,request.FILES,instance=car)
              if form.is_valid():
                  form.save()
                  for image in request.FILES.getlist('images'):
                      CarImage.objects.create(car=car,images=image)
                 
                      return redirect('carzz:home')
          else:
              form = DealerAddCarForm()
            #   car_image_form = DealerAddImagesForm()
              return render(request,'carzz/add_car.html',{'form':form,
                                                        'i_form':DealerAddImagesForm})
    return redirect('login')

def edit_car(request,id):
    if request.user.is_authenticated and request.user.is_dealer:
           car = get_object_or_404(Car,id=id)
           if request.method == 'POST':
               form = DealerAddCarForm(request.POST,request.FILES,instance=car)
               if form.is_valid():
                   form.save()
                   return redirect('carzz:dashboard',dealer_id=request.user.id)
           else:
               form = DealerAddCarForm(instance=car)
           return render(request,'carzz/add_car.html', {'form':form})