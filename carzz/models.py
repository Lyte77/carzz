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
    dealer = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    mileage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

  # For storing car images

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) belongs to {self.dealer}"
        
    