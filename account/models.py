from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.contrib import messages


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,email, password=None,**extra_fields):
        if not email:
            raise ValueError('Invalid email address was entered')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        else:
            raise ValueError("The Password field must be set")

        user.save(using=self._db)
        return user

    def create_superuser(self,email, password,**extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email,password,**extra_fields)
    




class CustomUser(AbstractBaseUser, PermissionsMixin):

   
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(unique=True)
    is_dealer = models.BooleanField(default=False, blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name","is_dealer"]

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f"{self.first_name} - {self.last_name}"

  

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    
   