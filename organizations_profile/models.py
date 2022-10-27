from django.conf import settings
from django.db import models
from authentication.models import User
from homepage.models import Donation

# Create your models here.
'''class Donation_List(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        on_delete=models.CASCADE
    )
    donation = models.OneToManyField(
        Donation,
        null=True,
        on_delete=models.SET_NULL
    )'''

