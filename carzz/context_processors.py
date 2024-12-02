from .models import DealerProfileModel
from django.shortcuts import get_object_or_404

def dealer_profile_context(request):
    if request.user.is_authenticated and hasattr(request.user, 'is_dealer') and request.user.is_dealer:
        dealer_profile = get_object_or_404(DealerProfileModel, user=request.user)
        print(dealer_profile.name)
        return {'dealer_profile': dealer_profile}
    return {}

# def check_if_dealer_has_profile(request,user):
#     if request.user.is_authenticated and hasattr(request.user, 'is_dealer') and request.user.is_dealer:
#         has_profile = DealerProfileModel.objects.filter(name=user).exists()
#         if has_profile:
#             print('You already have a profile')
#         else:
#             print("Create a profile")
#         return {'has_profile': has_profile}
#     return {}
