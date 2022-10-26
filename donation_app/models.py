from django.db import models
from authentication.models import User

# Create your models here.

class Donation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) # organisasi yang bikin donasi
    title = models.CharField(max_length=255) # judul donasi
    description = models.TextField() # deskripsi donasi
    date_created = models.DateField()
    date_expired = models.DateField()
    money_accumulated = models.IntegerField(default=0)

    # is_finished = models.BooleanField(default=False) # buat stop donasi

