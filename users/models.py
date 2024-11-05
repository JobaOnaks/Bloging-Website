from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)