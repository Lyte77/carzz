from django.shortcuts import render, redirect, get_object_or_404
from .forms import (DealerProfileForm,
                    DealerEditProfileForm,
                    UserProfileForm,
                    UserEditProfileForm)
from django.core.exceptions import ValidationError
from account.models import CustomUser
from .forms import (DealerAddCarForm,                  
                     CarImageFormSet)
from .models import Car, CarImage, SavedCar
from django.db.models import Q, Sum
from django.contrib import messages
from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from django.http import HttpResponseForbidden, HttpResponse

from .models import DealerProfileModel, UserProfileModel
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
            no_of_cars = dealer_cars.count()

            print( f"No of cars : {no_of_cars}")

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
                      'no_of_cars':no_of_cars,
                      }
            return render(request, 'carzz/dashboard.html',context)
    return HttpResponse()
    

def user_dashboard(request,user_id):
    user_profile = get_object_or_404(UserProfileModel, user_id=user_id)
    car =  Car.objects.all()
    saved_car =  SavedCar.objects.filter(user=request.user).select_related('car')
 
    context = {'user_profile':user_profile,
               'saved_car':saved_car,
               'saved_cars':[saved_car.car for saved_car in saved_car]}
    
    return render(request, 'carzz/user_dashboard.html', context)



        

            
            
           
                       

        

def dealer_profile(request,dealer_id):
   dealer_profile = get_object_or_404(DealerProfileModel,user_id=dealer_id)

   context = {'dealer_profile':dealer_profile,
             }
   return render(request,'carzz/dealer_profile.html',context)

def user_profile(request,user_id):
   user_profile = get_object_or_404(UserProfileModel,user_id=user_id)
  
   context = {'user_profile':user_profile,
             }
   return render(request,'carzz/user_profile.html',context)








def create_profile(request):
    
        if request.method == 'POST':
             form = DealerProfileForm(request.POST,files=request.FILES)
             if form.is_valid():
                  profile = form.save(commit=False)
                  profile.user = request.user
                  profile.save()
                  messages.success(request, 'Profile Created')
                  return redirect('carzz:home')
        else:
             form = DealerProfileForm()
        return render(request, 'carzz/profile_form.html', {'form':form})


def create_user_profile(request):
    if request.method =='POST':
        form = UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
             profile = form.save(commit=False)
             profile.user = request.user
             profile.save()
             messages.success(request, 'Profile Created')
             return redirect('carzz:home')
    else:
        form = UserProfileForm()
    return render(request,'carzz/user_profile_form.html',{'profile_form':form})



          
                  
    
     
        
        
        





def update_dealer_profile(request):
     if request.user.is_authenticated and request.user.is_dealer:
       
        dealer = DealerProfileModel.objects.get(user=request.user)
        form = DealerEditProfileForm(instance=dealer)
        if request.method == 'POST':
            form = DealerEditProfileForm(request.POST,request.FILES,instance=dealer)
            if form.is_valid():
                 form.save()
            try:
                email_address = EmailAddress.objects.get(user=request.user, primary=True)
                if email_address.verified:
                    messages.success(request, 'Profile Updated')
                    return redirect('carzz:dealer_dashboard', dealer_id=request.user.id)
                else:
                    return redirect('carzz:profile-verify-email')
            except EmailAddress.DoesNotExist:
                    messages.error(request, 'Primary email not found. Please verify your email.')
                    return redirect('carzz:profile-verify-email')
            
    
                 
        
        return render(request,'carzz/dealer_edit_form.html',{'form':form})
     return HttpResponse()

def update_user_profile(request):
 if request.user.is_authenticated and not request.user.is_dealer:
     user = UserProfileModel.objects.get(user=request.user)
     form = DealerEditProfileForm(instance=user)
     if request.method == 'POST':
            form = UserEditProfileForm(request.POST,request.FILES,instance=user)
            if form.is_valid():
                 form.save()
            try:
                email_address = EmailAddress.objects.get(user=request.user, primary=True)
                if email_address.verified:
                    messages.success(request, 'Profile Updated')
                    return redirect('carzz:user_dashboard', user_id=request.user.id)
                else:
                    return redirect('carzz:profile-verify-email')
            except EmailAddress.DoesNotExist:
                    messages.error(request, 'Primary email not found. Please verify your email.')
                    return redirect('carzz:profile-verify-email')
            
     return render(request,'carzz/user_edit_form.html',{'profile_form':form})
 return HttpResponse()


def add_car(request):
    # Ensure the user is authenticated and has the correct role
    if request.user.is_authenticated and request.user.is_dealer:
        # Handle POST requests for car and images
        if request.method == 'POST':
            # Initialize the car object with the current dealer
            car = Car(dealer=DealerProfileModel.objects.get(user=request.user))

            # Bind forms and formsets to POST data and files
            car_form = DealerAddCarForm(request.POST, request.FILES, instance=car)
            formset = CarImageFormSet(request.POST, request.FILES, queryset=CarImage.objects.none())

            if car_form.is_valid() and formset.is_valid():
                # Save the car object
                car = car_form.save()

                # Save all the valid images from the formset
                for form in formset:
                    if form.cleaned_data:
                        car_image = form.save(commit=False)
                        car_image.car = car
                        car_image.save()

                # Display a success message and redirect to the dashboard
                messages.success(request, 'Car added successfully.')
                return redirect('carzz:dealer_dashboard', dealer_id=request.user.id)
            else:
                # Handle form and formset errors
                messages.error(request, 'There was an issue adding your car. Please check the form and try again.')

        else:  # Handle GET requests by displaying empty forms
            car_form = DealerAddCarForm()
            formset = CarImageFormSet(queryset=CarImage.objects.none())

        # Render the add_car template
        return render(request, 'carzz/add_car.html', {
            'car_form': car_form,
            'formset': formset
        })

    # Redirect unauthenticated users to the login page
    return redirect('login')
             
                 
                 
             
                                                        



        


def edit_car(request, id):
    # Ensure the user is authenticated and a dealer
    if request.user.is_authenticated and request.user.is_dealer:
        # Get the car object or return a 404 if not found
        car = get_object_or_404(Car, id=id, dealer__user=request.user)

        # Initialize the formset with the car's images
        formset = CarImageFormSet(queryset=CarImage.objects.filter(car=car))

        if request.method == 'POST':
            print(request.POST)
            print(request.FILES)
            # Bind the forms and formset to the POST data
            car_form = DealerAddCarForm(request.POST, request.FILES, instance=car)
            formset = CarImageFormSet(request.POST or None, request.FILES or None, queryset=CarImage.objects.filter(car=car))

            if car_form.is_valid():
                # Save the car form
                car_form.save()

                # Process each form in the formset
                if formset.is_valid():
                        for form in formset:
                            if form.cleaned_data:
                                if form.cleaned_data.get('DELETE'):
                                    form.instance.delete()
                                else:
                                # Save the updated or new image
                                    car_image = form.save(commit=False)
                                    car_image.car = car
                                    car_image.save()
                else:
                     print("Formset Errors:", formset.errors)

                # Display a success message and redirect to the dashboard
                messages.success(request, 'Car updated successfully.')
                return redirect('carzz:dealer_dashboard', dealer_id=request.user.id)
            

                
            else:
                messages.error(request, 'There was an issue updating the car. Please check the form and try again.')

        else:
            # Initialize the forms with existing data
            car_form = DealerAddCarForm(instance=car)

        # Render the edit car template
        return render(request, 'carzz/update_car.html', {
            'car_form': car_form,
            'formset': formset
        })

   
    return redirect('login')





def delete_car(request, id):

    car = get_object_or_404(Car,id=id)
    car.delete()
    messages.success(request,"Car deleted Sucessfully")
    return redirect('carzz:dealer_dashboard',request.user.id)

def save_car(request,car_id):
     car = get_object_or_404(Car, id=car_id)
     saved_car, created = SavedCar.objects.get_or_create(user=request.user,car=car)

     if created:
          messages.success(request,f'{car.model} has been saved to your dashboard')
     else:
         messages.info(request, f'{car.model} is already saved')
          
     return redirect('carzz:user_dashboard', user_id=request.user.id)

def delete_saved_car(request,car_id):
    car = get_object_or_404(Car, id=car_id)
    # saved_car = SavedCar.objects.filter(user=request.user,car=car).select_related('car')
    saved_car = get_object_or_404(SavedCar, user=request.user, car_id=car_id)
    saved_car.delete()
    messages.success(request,'Car removed')
    return redirect('carzz:user_dashboard',request.user.id)

def profile_verify_email(request):
     send_email_confirmation(request, request.user)
     return redirect('carzz:dealer_dashboard', dealer_id=request.user.id)