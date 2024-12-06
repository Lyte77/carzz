from django.contrib import admin
from .models import DealerProfileModel, Car,CarImage,UserProfileModel

# Register your models here.

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]


@admin.register(UserProfileModel)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','phone_number', 'date_joined')

admin.site.register(DealerProfileModel)
# admin.site.register(Car)
# admin.site.register(CarImage)
