from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    fullname = models.CharField(blank=False,max_length=255)
    email = models.CharField(blank=False,unique=True,max_length=255)
    phone = models.CharField(blank=False,max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname","phone"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email