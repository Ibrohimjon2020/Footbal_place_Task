from django.contrib.auth.models import AbstractUser
from django.db import models

from .manager import UserManager


class User(AbstractUser):
    username = None
    role = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12, unique=True)
    otp_code = models.CharField(max_length=6, null=True)
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    address = models.TextField(null=True)
    objects = UserManager()

    def __str__(self):
        return self.first_name