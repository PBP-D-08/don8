from unittest.util import _MAX_LENGTH
from django.db import models
from authentication.models import User
import datetime
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_name = models.TextField(null = True)
    donation_name = models.CharField(max_length = 255)
    message = models.TextField()
    date_created = models.DateField(default=datetime.date.today)
    likes = models.ManyToManyField(User, related_name='post_like')

    @property
    def num_likes(self):
        return self.likes.count()
