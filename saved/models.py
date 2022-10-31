from django.db import models
from authentication.models import User
from homepage.models import Donation

# Create your models here.
class SavedDonation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="saved")
    donation = models.ForeignKey(
        Donation, on_delete=models.CASCADE, related_name="saved"
    )
