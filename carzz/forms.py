from django import forms
from django.forms import modelformset_factory
from .models import (DealerProfileModel, 
                     Car,
                    CarImage,
                    UserProfileModel)

class DealerProfileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Name',
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

    pic = forms.ImageField(widget=forms.FileInput(

    ))
    class Meta:
        model = DealerProfileModel
        fields = ['name','phone_number','address',
                  'social_media','years_in_business','pic']

      
class DealerEditProfileForm(forms.ModelForm):
     name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Name',
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
     pic = forms.CharField(widget=forms.FileInput(
         attrs={
            
         }
     ))
     class Meta:
        model = DealerProfileModel
        fields = ['name','phone_number','address',
                  'social_media','years_in_business','pic']
        
class UserProfileForm(forms.ModelForm):
     profile_picture = forms.ImageField(widget=forms.FileInput(

    ))
     phone_number = forms.CharField(widget=forms.NumberInput(
         attrs={
             'class':'w-full px-8 py-4 mb-5 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm   focus:bg-white'
         }
     ))
     address = forms.CharField(widget=forms.TextInput(
         attrs={
             'class':'w-full px-8 py-4 mb-5 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm   focus:bg-white'
         }
     ))

     class Meta:
        model = UserProfileModel
        fields = ['profile_picture','phone_number','address']
        

class DealerAddCarForm(forms.ModelForm):
    make = forms.CharField(widget=forms.TextInput(
        attrs= {
            'class':'h-10 border mt-1 rounded px-4 w-full bg-gray-50"',
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
        fields = [  'image','view_type']
    
    
CarImageFormSet = modelformset_factory(
    CarImage,
    form=DealerAddImagesForm,
    extra=3,
    can_delete=True

)