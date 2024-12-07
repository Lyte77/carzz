from django import forms
from django.forms import modelformset_factory
from .models import (DealerProfileModel, 
                     Car,
                    CarImage,
                    UserProfileModel)

class DealerProfileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Name'
        }
    ))

    pic = forms.ImageField(widget=forms.FileInput(

    ))
    class Meta:
        model = DealerProfileModel
        fields = ['name','phone_number','address','website',
                  'social_media','years_in_business','pic']

      
class DealerEditProfileForm(forms.ModelForm):
    class Meta:
        model = DealerProfileModel
        fields = ['name','phone_number','address','website',
                  'social_media','years_in_business','pic']
        
class UserProfileForm(forms.ModelForm):
     profile_picture = forms.ImageField(widget=forms.FileInput(

    ))

     class Meta:
        model = UserProfileModel
        fields = ['profile_picture','phone_number','address']
        

class DealerAddCarForm(forms.ModelForm):
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