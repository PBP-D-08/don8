from email import message
from email.policy import default
import imp
from django.db import models
from authentication.models import User
import datetime
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_created = models.DateField(default=datetime.date.today)
    likes = models.IntegerField(default=0)