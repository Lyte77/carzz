from django.shortcuts import render, redirect, get_object_or_404
from .forms import DealerProfileForm,DealerEditProfileForm
from django.core.exceptions import ValidationError
from account.models import CustomUser
from .forms import DealerAddCarForm, DealerAddImagesForm, CarImageFormSet
from .models import Car, CarImage
from django.db.models import Q
from django.http import HttpResponseForbidden

from .models import DealerProfileModel
# Create your views here.

def home_page(request):
    query =  request.GET.get('query','')
    cars = Car.objects.all()

    if query:
        cars = cars.filter(
            Q(make__icontains=query) | 
            Q(model__icontains=query) | 
            Q(year__icontains=query))
    context = {'cars':cars,
               'query':query,}
    return render(request, 'carzz/home.html',context)
        
                   
       
    
    

def car_detail_page(request,id):
    car = get_object_or_404(Car,id=id)
    images = car.images.all()
    
    context = {'car':car,
               'images':images
              
               }
    return render(request,'carzz/car_detail.html',context)



def dashboard(request, dealer_id):
    if request.user.is_authenticated and request.user.is_dealer:
            if request.user.id != dealer_id:
                return HttpResponseForbidden("You cant acces this dashboard")
            dealer = request.user
            
            dealer_profile =  get_object_or_404(DealerProfileModel,user_id=dealer_id)
            dealer_cars = Car.objects.filter(dealer=dealer_profile).prefetch_related('images')
            print(dealer_cars)
            
            
           
            context = {'dealer':dealer,
                      'dealer_profile':dealer_profile,
                      'dealer_cars':dealer_cars,
                    #   'dealer_images':dealer_images
                      }
                       
            return render(request, 'carzz/dashboard.html',context)

        

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
    if request.user.is_authenticated and request.user.is_dealer:
     
          
          if request.method == 'POST':
              car = Car(dealer=DealerProfileModel.objects.get(user=request.user))
              car.save()
           
             
              car_form = DealerAddCarForm(request.POST,request.FILES,instance=car)
              formset = CarImageFormSet(request.POST,request.FILES,queryset=CarImage.objects.none())
              if car_form.is_valid() and formset.is_valid():
                  car_form.save()

                  for form in formset:
                      if form.cleaned_data:
                          car_image = form.save(commit=False)
                          car_image.car = car
                          car_image.save()
              return redirect('carzz:dashboard',dealer_id=request.user.id)
               
          else:
              car_form = DealerAddCarForm()
              formset = CarImageFormSet(queryset=CarImage.objects.none())
              return render(request,'carzz/add_car.html',{
                  'car_form':car_form,
                  'formset':formset
                  })
    return redirect('login')


             
                 
                 
             
                                                        



def edit_car(request,id):
    if request.user.is_authenticated and request.user.is_dealer:
           car = get_object_or_404(Car,id=id)
           formset = CarImageFormSet(queryset=CarImage.objects.filter(car=car)) 

           if request.method == 'POST':
               car_form = DealerAddCarForm(request.POST,request.FILES,instance=car)
               formset = CarImageFormSet(request.POST,request.FILES,queryset=CarImage.objects.filter(car=car))

               if car_form.is_valid() and formset.is_valid():
                   car_form.save()
                   
                   for form in formset:
                       if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                           car_image = form.save(commit=False)
                           car_image.car = car
                           car_image.save()
                       elif form.cleaned_data.get('DELETE'):
                           form.instance.delete()
                   return redirect('carzz:dashboard',dealer_id=request.user.id)
           else:
               car_form = DealerAddCarForm(instance=car)
               formset = CarImageFormSet(queryset=CarImage.objects.filter(car=car))

           return render(request,'carzz/add_car.html', {'car_form':car_form,
                                                        'formset':formset})
    
def delete_car(request, id):
    car = get_object_or_404(Car,id=id)
    car.delete()
    return redirect('carzz:dashboard',request.user.id)