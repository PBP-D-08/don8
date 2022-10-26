from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# user abstract user
class User(AbstractUser):

    USER = 1
    COMPANY = 2

    ROLE_CHOICES = (
        (USER, "user"),
        (COMPANY, "company"),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=USER)

    balance = models.IntegerField(default=0)
