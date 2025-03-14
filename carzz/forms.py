from django import forms
from django.forms import modelformset_factory
from .models import (DealerProfileModel, 
                     Car,
                    CarImage,
                    UserProfileModel
                    )

class DealerProfileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Name',
            'class':'h-10 border mt-1 rounded px-4 w-full bg-gray-50'
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder':'Email',
            'class':'h-10 border mt-1 rounded px-4 w-full bg-gray-50'
        }
    ))
    phone_number = forms.CharField(widget=forms.NumberInput(
         attrs={
            'class':'mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800' 
         }
     ))
    address = forms.CharField(widget=forms.TextInput(
         attrs={
            'class':'mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800'
         }
     ))
    social_media = forms.CharField(widget=forms.TextInput(
         attrs={
             'class':'mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800'
         }
     ))
    years_in_business = forms.CharField(widget=forms.NumberInput(
         attrs={
             'class':'mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800'
         }
     ))

    pic = forms.FileField()   
    class Meta:
        model = DealerProfileModel
        fields = ['name', 'email' ,'phone_number','address',
                  'social_media','years_in_business','pic']

      
class DealerEditProfileForm(forms.ModelForm):
     name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Name',
            'class':'h-10 border mt-1 rounded px-4 w-full bg-gray-50',
            'id':'id_name'
        }
    ))
     email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder':'Email',
            'class':'h-10 border mt-1 rounded px-4 w-full bg-gray-50'
        }
    ))
     phone_number = forms.CharField(widget=forms.NumberInput(
         attrs={
            'class':'mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800' 
         }
     ))
     address = forms.CharField(widget=forms.TextInput(
         attrs={
            'class':'mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800'
         }
     ))
     
    
     social_media = forms.CharField(widget=forms.TextInput(
         attrs={
             'class':'mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800'
         }
     ))
     years_in_business = forms.CharField(widget=forms.NumberInput(
         attrs={
             'class':'mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800'
         }
     ))
     pic = forms.FileField()   
        
    
     class Meta:
        model = DealerProfileModel
        fields = ['name', 'email', 'phone_number','address',
                  'social_media','years_in_business','pic']
        
class DealerAddCarForm(forms.ModelForm):
    make = forms.CharField(widget=forms.TextInput(
        attrs= {
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm focus:outline-none  focus:bg-white mt-5',
        }
    ))
    model = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm focus:outline-none  focus:bg-white mt-5'
        }
    ))
    year = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm focus:outline-none  focus:bg-white mt-5'
        }
    ))
    mileage = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm focus:outline-none  focus:bg-white mt-5'
        }
    ))
    thumbnail = forms.FileField(widget=forms.FileInput(
        attrs={
            # 'class':'  px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm focus:outline-none  focus:bg-white mt-5'
        }
    ))
    price = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm focus:outline-none  focus:bg-white mt-5'
        }
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm focus:outline-none  focus:bg-white mt-5'
        }
    ))
    
    class Meta:
        model = Car
        fields = ['make','model','year','mileage','thumbnail','price','description']
    # images= forms.FileField(widget=forms.ClearableFileInput,
    #                         )

class DealerAddImagesForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields = [ 'image','view_type']
    
    
CarImageFormSet = modelformset_factory(
   
    CarImage,
     fields=['id', 'image','view_type'],
    form=DealerAddImagesForm,
    extra=3,
    can_delete=True

)

class DealerEditCar(forms.ModelForm):
    make = forms.CharField(widget=forms.TextInput(
        attrs= {
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm focus:outline-none  focus:bg-white mt-5',
        }
    ))
    model = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm focus:outline-none  focus:bg-white mt-5'
        }
    ))
    year = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm focus:outline-none  focus:bg-white mt-5'
        }
    ))
    mileage = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm focus:outline-none  focus:bg-white mt-5'
        }
    ))
    thumbnail = forms.FileField(widget=forms.FileInput(
        attrs={
            # 'class':'  px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm focus:outline-none  focus:bg-white mt-5'
        }
    ))
    price = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm focus:outline-none  focus:bg-white mt-5'
        }
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'w-full px-8 py-4 rounded-lg font-medium  border border-red-700  text-sm focus:outline-none  focus:bg-white mt-5'
        }
    ))


    class Meta:
        model = Car
        fields = ['make','model','year','mileage','thumbnail','price','description']


# Users Profile Section

class UserProfileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Name',
            'class':'h-10 border mt-1 rounded px-4 w-full bg-gray-50'
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder':'Email',
            'class':'h-10 border mt-1 rounded px-4 w-full bg-gray-50'
        }
    ))
    phone_number = forms.CharField(widget=forms.NumberInput(
         attrs={
            'class':'mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800' 
         }
     ))
    address = forms.CharField(widget=forms.TextInput(
         attrs={
            'class':'mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800'
         }
     ))
    
    

    profile_picture = forms.FileField()  
    class Meta:
        model = UserProfileModel
        fields = ['name','email','phone_number','address','profile_picture']

class UserEditProfileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Name',
            'class':'h-10 border mt-1 rounded px-4 w-full bg-gray-50'
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder':'Email',
            'class':'h-10 border mt-1 rounded px-4 w-full bg-gray-50'
        }
    ))
    phone_number = forms.CharField(widget=forms.NumberInput(
         attrs={
            'class':'mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800' 
         }
     ))
    address = forms.CharField(widget=forms.TextInput(
         attrs={
            'class':'mt-2 p-4 w-full border-2 rounded-lg dark:text-gray-200 dark:border-gray-600 dark:bg-gray-800'
         }
     ))
    
    

    profile_picture = forms.FileField()  
    class Meta:
        model = UserProfileModel
        fields = ['name','email','phone_number','address','profile_picture']