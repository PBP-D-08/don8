from django.conf import settings
from django.db import models
from authentication.models import User


class Profile(models.Model):
    organization = models.OneToOneField(User, on_delete=models.CASCADE, related_name="company_profile")
    withdrawn = models.IntegerField(default=0)
    total_campaign = models.IntegerField(default=0)

