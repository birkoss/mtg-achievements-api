from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.models import TimeStampedModel, UUIDModel

from .managers import UserManager


class User(PermissionsMixin, UUIDModel, TimeStampedModel, AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    name = models.CharField(max_length=100, default='')

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email
