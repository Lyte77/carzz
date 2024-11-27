from django.contrib import admin
from .models import CustomUser
from carzz.models import DealerProfileModel

# Register your models here.


# admin.site.register(CustomUser)
class ProfileInLine(admin.StackedInline):
    model = DealerProfileModel


class UserAdmin(admin.ModelAdmin):
    model = CustomUser
    inlines = [ProfileInLine]
    

admin.site.register(CustomUser,UserAdmin)