from django import forms
from authentication.models import User
from donation_app.models import UserDonation
from homepage.models import Donation
import datetime

class DonationForm(forms.ModelForm):
    class Meta:
        model = UserDonation
        fields = ["amount_of_donation"]
        widgets = {
            "amount_of_donation": forms.NumberInput(attrs={"class" : "border-2 border-blue-500 rounded border-black"})
        }

    def save(self, request, donation_id):

        user = request.user
        donation = Donation.objects.get(id=donation_id)
        amount_of_donation = self.cleaned_data.get("amount_of_donation")

        if user.balance - amount_of_donation >= 0:

            donation.money_accumulated = donation.money_accumulated + amount_of_donation
            user.balance = user.balance - amount_of_donation

            UserDonation.objects.create(
                user = user,
                organization = donation.user,
                donation = donation,
                date = datetime.date.today(),
                amount_of_donation = amount_of_donation
            )

            donation.save()
            user.save()

            data = {"message": "success", "money_accumulated": donation.money_accumulated, "money_needed": donation.money_needed}

        else:
            data = {"message": "Uang tidak cukup", "money_accumulated": donation.money_accumulated, "money_needed": donation.money_needed}

        return data