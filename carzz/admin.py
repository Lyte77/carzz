from django.contrib import admin
from .models import DealerProfileModel, Car,CarImage

# Register your models here.
admin.site.register(DealerProfileModel)
admin.site.register(Car)
admin.site.register(CarImage)
