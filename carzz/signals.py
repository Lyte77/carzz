from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import CustomUser
from .models import DealerProfileModel
from allauth.account.models import EmailAddress

# @receiver(post_save,sender=CustomUser)
# def create_dealer_profile(sender,instance,created,**kwargs):
#     if created and getattr(instance,'is_dealer',False):
#         DealerProfileModel.objects.create(user=instance)

# @receiver(post_save,sender=CustomUser)
# def save_dealer_profile(sender,instance,**kwargs):
#     if hasattr(instance,'dealer_profile'):
#         instance.dealer_profile.save()

@receiver(post_save, sender=DealerProfileModel)
def update_account_email(sender,instance,created,**kwargs):
    profile = instance
    if not created:
        try:
            email_address = EmailAddress.objects.get_primary(profile.user)
            if email_address.email != profile.email:
                email_address.email = profile.email
                email_address.verified = False
                email_address.save()
        except:
            pass