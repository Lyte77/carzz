from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from account.models import CustomUser
from django.db.models.signals import post_save

# Create your models here.


class DealerProfileModel(models.Model):
        user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,primary_key=True)
        name = models.CharField(max_length=200, blank=False)
        phone_number = models.CharField(max_length=20, blank=False)
        # email = models.EmailField(unique=True, blank=False)
        address = models.CharField(blank=False, max_length=200)
        website = models.URLField(blank=True)
        social_media = models.CharField(max_length=400)
        years_in_business = models.IntegerField(blank=True,null=True)
        pic = models.ImageField(blank=True, upload_to='profile-img/%Y/%m/%d/')
        date_joined = models.DateTimeField(auto_now_add=True,null=True)

        def __str__(self):
            return self.user.email
        
# def create_profile(sender,instance,created,**kwargs):
#       if created:
#             user_profile = DealerProfileModel(user=instance)
#             user_profile.save()
# post_save.connect(create_profile,sender=CustomUser)


class Car(models.Model):
    dealer = models.ForeignKey(DealerProfileModel,on_delete=models.CASCADE,related_name='cars')
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    mileage = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    thumbnail = models.ImageField(upload_to='car_images/',null=True)
    description = models.TextField(null=True)

  

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) belongs to {self.dealer}"
    

class CarImage(models.Model):
     car = models.ForeignKey(Car,on_delete=models.CASCADE,related_name='images')
     name = models.CharField(max_length=200, blank=True,null=True)
     images = models.ImageField(upload_to='car_images/')

     def __str__(self):
          return self.car.make
    