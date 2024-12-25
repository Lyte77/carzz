from django.shortcuts import render, redirect, get_object_or_404
from .forms import DealerProfileForm,DealerEditProfileForm
from django.core.exceptions import ValidationError
from account.models import CustomUser
from .forms import (DealerAddCarForm,
                     UserProfileForm,
                     UserProfileModel,
                     CarImageFormSet)
from .models import Car, CarImage, SavedCar
from django.db.models import Q, Sum
from django.contrib import messages
from django.http import HttpResponseForbidden, HttpResponse

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

def coming_soon_page(request):
     return render(request,'carzz/coming_soon.html')
        
                   
       
    
    

def car_detail_page(request,id):
    car = get_object_or_404(Car,id=id)
    car.views += 1
    car.save()
    images = car.images.all()
    context = {'car':car,
               'images':images
               }
    return render(request,'carzz/car_detail.html',context)
   
    
              

def dashboard_router(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.user.is_dealer:
        return redirect('carzz:dealer_dashboard', dealer_id=request.user.id)
    else:
        return redirect('carzz:user_dashboard', user_id=request.user.id)




def dealer_dashboard(request, dealer_id):
    if request.user.is_authenticated and request.user.is_dealer:
            if request.user.id != dealer_id:
                return HttpResponseForbidden("You cant acces this dashboard")
            dealer = request.user
            
            dealer_profile =  get_object_or_404(DealerProfileModel,user_id=dealer_id)
            dealer_cars = Car.objects.filter(dealer=dealer_profile).prefetch_related('images')
            total_views = dealer_cars.aggregate(Sum('views'))['views__sum'] or 0
            no_of_sold_cars = dealer_cars.filter(sold=True).count()

            if request.method == 'POST' and 'mark_as_sold' in request.POST:
                car_id = request.POST.get('car_id')
                car = get_object_or_404(Car, id=car_id,dealer=dealer_profile)
                car.sold = True
                car.save()
            if request.method == 'POST' and 'unmark_as_sold' in request.POST:
                car_id = request.POST.get('car_id')
                car = get_object_or_404(Car, id=car_id,dealer=dealer_profile)
                car.sold = False
                car.save()
            
            print(total_views)
            context = {'dealer':dealer,
                      'dealer_profile':dealer_profile,
                      'dealer_cars':dealer_cars,
                      'total_views': total_views,
                      'no_of_sold_cars':no_of_sold_cars,
                      }
            return render(request, 'carzz/dashboard.html',context)
    

def user_dashboard(request, user_id):
        if not request.user.is_authenticated:
                return redirect('login')

        if request.user.id != user_id:
                return HttpResponseForbidden("You can't access this dashboard")
        user = request.user
        try:
                    user_profile =  get_object_or_404(UserProfileModel,user_id=user_id)
                    saved_car = SavedCar.objects.filter(user=request.user).select_related('car')
                    context = {'user':user,
                            'user_profile':user_profile,
                            'saved_car':saved_car,
                            'saved_cars': [saved_car.car for saved_car in saved_car]}
                    return render(request,'carzz/user_dashboard.html',context)
        
        except Exception as e:
        # Return an error response if something unexpected happens
            return HttpResponse(f"An error occurred: {str(e)}", status=500)
                


        

            
            
           
                       

        

def dealer_profile(request,dealer_id):
   dealer_profile = get_object_or_404(DealerProfileModel,user_id=dealer_id)
  
   context = {'dealer_profile':dealer_profile,
             }
   return render(request,'carzz/dealer_profile.html',context)


def setup_profile(request):
    if request.user.is_authenticated and request.user.is_dealer:
            try:
                if request.method == 'POST':
                    profile_form = DealerProfileForm(request.POST, request.FILES)
                    if profile_form.is_valid():
                        profile = profile_form.save(commit=False)  # Avoid unnecessary database write-through
                        profile.user = request.user
                        profile.save()
                        print("updated")
                        messages.success(request, 'Profile Updated')
                        return redirect('carzz:dealer_dashboard', request.user.id)
                else:
                    profile_form = DealerProfileForm()
            except Exception as e:
                 return HttpResponse(f"An error occurred: {str(e)}", status=500)
            return render(request, 'carzz/profile_form.html',{'profile_form':profile_form})
    else:
        
        return redirect('login')  
    


def setup_user_profile(request):
    if request.user.is_authenticated and not request.user.is_dealer:
        if request.method == 'POST':
            profile_form = UserProfileForm(request.POST,files=request.FILES)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = request.user
                profile.save()
                messages.success(request, 'Profile Updated')


                return redirect('carzz:user_dashboard', request.user.id)

        else:
            profile_form = UserProfileForm()
        return render(request, 'carzz/user_profile_form.html',{'profile_form':profile_form})
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
                    messages.success(request, 'Profile Updated')
                    
                    return redirect('carzz:dealer_dashboard', dealer_id=request.user.id)
            else:
                current_profile = DealerProfileModel.objects.get(user=request.user)
                form = DealerEditProfileForm(instance=current_profile)
            return render(request, 'carzz/profile_form.html',{'profile_form':form})
        
    

def update_user_profile(request):
     if request.user.is_authenticated:
          if request.method == 'POST':
               current_profile = UserProfileModel.objects.get(user=request.user)

               
               form = UserProfileForm(data=request.POST,
                                      files=request.FILES,
                                      instance=current_profile)
               if form.is_valid():
                    form.save()
                    messages.success(request, 'Profile Updated')

                    return redirect('carzz:user_dashboard',
                                    user_id=request.user.id)
          else:
               
               current_profile = UserProfileModel.objects.get(user=request.user)
               form = UserProfileForm(instance=current_profile)
          return render(request, 'carzz/user_profile_form.html',{'form':form})


def add_car(request):
    if request.user.is_authenticated and request.user.is_dealer:
     
          
          if request.method == 'POST':
              car = Car(dealer=DealerProfileModel.objects.get(user=request.user))
              car.save()
           
             
              car_form = DealerAddCarForm(request.POST,request.FILES,instance=car)
              formset = CarImageFormSet(request.POST,request.FILES,queryset=CarImage.objects.none())
              if car_form.is_valid() and formset.is_valid():
                  car_form.save()
                  messages.success(request,'Car added Sucessfully')
              else:
                     messages.error(request, 'There is an issue adding your cars')
                          

              for form in formset:
                      if form.cleaned_data:
                          car_image = form.save(commit=False)
                          car_image.car = car
                          car_image.save()
                      
              return redirect('carzz:dealer_dashboard',dealer_id=request.user.id)
               
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
                           messages.success(request,'Car Updated')
                       elif form.cleaned_data.get('DELETE'):
                           form.instance.delete()
                   return redirect('carzz:dealer_dashboard',dealer_id=request.user.id)
           else:
               car_form = DealerAddCarForm(instance=car)
               formset = CarImageFormSet(queryset=CarImage.objects.filter(car=car))

           return render(request,'carzz/add_car.html', {'car_form':car_form,
                                                        'formset':formset})
    
def delete_car(request, id):
    car = get_object_or_404(Car,id=id)
    car.delete()
    return redirect('carzz:dealer_dashboard',request.user.id)

def save_car(request,car_id):
     car = get_object_or_404(Car, id=car_id)
     saved_car, created = SavedCar.objects.get_or_create(user=request.user,car=car)

     if not created:
          saved_car.delete()
          messages.success(request,'Car Saved')
     return redirect('carzz:user_dashboard', user_id=request.user.id)