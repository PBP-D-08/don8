from django.conf import settings
from django.db import models

# Create your models here.
class Donation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateField()
    date_expired = models.DateField()
    money_accumulated = models.IntegerField(default=0)
    image_url = models.TextField()