from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import CustomUser
from .models import DealerProfileModel

# @receiver(post_save,sender=CustomUser)
# def create_dealer_profile(sender,instance,created,**kwargs):
#     if created and getattr(instance,'is_dealer',False):
#         DealerProfileModel.objects.create(user=instance)

# @receiver(post_save,sender=CustomUser)
# def save_dealer_profile(sender,instance,**kwargs):
#     if hasattr(instance,'dealer_profile'):
#         instance.dealer_profile.save()