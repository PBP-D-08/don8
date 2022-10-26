from django.shortcuts import render
from homepage.models import Donation
from authentication.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse

# Create your views here.

def show_donation_page(request, id):

    context = {
        "donation": Donation.objects.get(id=id)
    }
    return render(request, "donation_page.html", context)

# fungsi buat update wallet user dan cek apakah mencukupi atau tidak
def make_donation(request, id):

    if request.method == "POST":
        user = User.objects.get(user = request.user)
        donation = Donation.objects.get(id=id)
        money_accumulated = int(request.POST.get("money_accumulated"))

        if user.balance - money_accumulated >= 0:

            Donation.objects.get(id=id).update(money_accumulated = donation.money_accumulated + money_accumulated)
            User.objects.get(user = request.user).update(balance = user.balance - money_accumulated)
        else:
            #message
            ...

        # return HttpResponseRedirect(reverse("donation_app:show_donation_page"))
    

def update_money_accumulated(request, id):

    return

def show_json(request):
    donations = Donation.objects.all()
    return HttpResponse(
        serializers.serialize("json", donations), content_type="application/json"
    )

# mengambil data donasi dalam json by id
def get_donation_data(request, id):
    donation_data = Donation.objects.filter(id=id) # ganti jd ambil data user buat cek wallet
    return HttpResponse(serializers.serialize("json", donation_data), content_type="application/json")


