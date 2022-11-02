from django import forms
from authentication.models import User
from donation_app.models import UserDonation
from homepage.models import Donation
from organizations_profile.models import ProfileO
import datetime

class DonationForm(forms.ModelForm):
    class Meta:
        model = UserDonation
        fields = ["amount_of_donation"]
        widgets = {
            "amount_of_donation": forms.NumberInput(attrs={"class" : "border-2 border-blue-500 rounded border-black"})
        }

    def save(self, request, donation_id):

        user = request.user # user dengan role pengguna
        donation = Donation.objects.get(id=donation_id)
        organization = ProfileO.objects.get(organization=donation.user)
        amount_of_donation = self.cleaned_data.get("amount_of_donation", -1)

        if user.balance - amount_of_donation >= 0:

            donation.money_accumulated = donation.money_accumulated + amount_of_donation
            organization.total_campaign = organization.total_campaign + amount_of_donation
            donation.user.balance = donation.user.balance + amount_of_donation
            user.balance = user.balance - amount_of_donation

            UserDonation.objects.create(
                user = user,
                organization = donation.user,
                donation = donation,
                date = datetime.date.today(),
                amount_of_donation = amount_of_donation
            )

            donation.save()
            organization.save()
            user.save()
            donation.user.save()

            data = {"message": "Success", "money_accumulated": donation.money_accumulated, "money_needed": donation.money_needed}

        else:
            data = {"message": "Not enough money", "money_accumulated": donation.money_accumulated, "money_needed": donation.money_needed}

        return data