from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Donation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(validators=[MinLengthValidator(38)])
    date_created = models.DateField()
    date_expired = models.DateField()
    money_accumulated = models.IntegerField(default=0)
    money_needed = models.IntegerField(default=0)
    image_url = models.TextField()
