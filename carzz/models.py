from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from account.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver

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
        




class Car(models.Model):
    dealer = models.ForeignKey(DealerProfileModel,on_delete=models.CASCADE,related_name='cars')
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    mileage = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    thumbnail = models.ImageField(blank=True,null=True,upload_to='car_images/')
    description = models.TextField(null=True)
    views = models.PositiveIntegerField(default=0)
    sold = models.BooleanField(default=False)

  

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) belongs to {self.dealer}"
    

class CarImage(models.Model):
     car = models.ForeignKey(Car,on_delete=models.CASCADE,related_name='images')
     name = models.CharField(max_length=200, blank=True,null=True)
     image = models.ImageField(upload_to='car_images/')
     view_type = models.CharField(max_length=50,choices=[
          ('front','Front View'),
          ('rear','Rear View'),
          ('back','Back View'),
          ('interior','Interior View'),
          ('other','Other View'),
     ],
        default='other'
     )

     def __str__(self):
          return f'{self.car.dealer} - {self.get_view_type_display()}'
    

class UserProfileModel(models.Model):
     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_profile')
     profile_picture = models.ImageField(upload_to='profile-img/%Y/%m/%d/',blank=True, null=True)
     phone_number = models.CharField(max_length=15, blank=True,null=True)
     address = models.TextField(blank=True,null=True)

     favorites = models.ManyToManyField(Car,blank=True,related_name='favorited_by')
     search_history = models.JSONField(blank=True,null=True)

     date_joined = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return f"{self.user.first_name} 's Profile"
     

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
     if created and not instance.is_dealer:
          UserProfileModel.objects.create(user=instance)


class SavedCar(models.Model):
     user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
     car = models.ForeignKey(Car, on_delete=models.CASCADE)
     saved_at = models.DateTimeField(auto_now_add=True)

     class Meta:
          unique_together = ('user','car')

     def __str__(self):
          return f"{self.user.first_name} saved {self.car.model}"
        