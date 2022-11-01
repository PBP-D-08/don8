from django.db import models
from authentication.models import User
from homepage.models import Donation
from django.core.validators import MinValueValidator

# Create your models here.
class UserDonation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pengguna") # user dengan role pengguna
    organization = models.ForeignKey(User, on_delete=models.CASCADE, related_name="company") # user dengan role company
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    amount_of_donation = models.IntegerField(validators=[MinValueValidator(1)])