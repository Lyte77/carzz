from django import forms
from .models import DealerProfileModel

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
        fields = ['name','phone_number','email','address','website',
                  'social_media','years_in_business','pic']

      
class DealerEditProfileForm(forms.ModelForm):
    class Meta:
        model = DealerProfileModel
        fields = ['name','phone_number','email','address','website',
                  'social_media','years_in_business','pic']