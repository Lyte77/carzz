from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,email, password,**extra_fields):
        if not email:
            raise ValueError('Invalid email address was entered')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email, password,**extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email,password,**extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):

   
    first_name = models.CharField(max_length=100,blank=True,unique=True)
    last_name = models.CharField(max_length=100,blank=True,unique=True)
    email = models.EmailField(unique=True)
    is_dealer = models.BooleanField(default=False, blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email