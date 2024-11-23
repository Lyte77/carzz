from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from account.models import CustomUser

# Create your models here.

class DealerProfileModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=200, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    email = models.EmailField(unique=True, blank=False)
    address = models.CharField(blank=False, max_length=200)
    website = models.URLField(blank=True)
    social_media = models.CharField(max_length=400)
    years_in_business = models.IntegerField(blank=True,null=True)
    pic = models.ImageField(blank=True, upload_to='profile-img/%Y/%m/%d/')
    date_joined = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.user.email
