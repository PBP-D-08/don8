from django.db import models
from authentication.models import User

# Create your models here.
class ProfileU(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")    
    money_donated = models.IntegerField(default=0)
