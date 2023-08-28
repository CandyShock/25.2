from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='mail')

    phone = models.CharField(max_length=25, verbose_name='phone', **NULLABLE)
    country = models.CharField(max_length=25, verbose_name='country', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
