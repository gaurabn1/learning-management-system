from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    profile_img = models.ImageField(upload_to='profile_images', null=True, blank=True)
    
