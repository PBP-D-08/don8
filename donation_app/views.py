from django.shortcuts import render
from donation_app.models import Donation
# from 
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse

# Create your views here.

def show_donation_page(request, id):

    context = {
        "donation_data": Donation.objects.get(id=id)
    }
    return render(request, "donation_page", context)

# fungsi buat update wallet user dan cek apakah mencukupi atau tidak
def make_donation(request, id):

    if request.method == "POST":
        # user_data = User.objects.get(user = request.user)

        money_accumulated = int(request.POST.get("money_accumulated"))
        Donation.objects.get(id=id).update(money_accumulated=money_accumulated)

        # return HttpResponseRedirect(reverse("donation_app:show_donation_page"))
    

def update_money_accumulated(request, id):

    return

# # mengambil data donasi dalam json by id
# def get_donation_data(request, id):
#     donation_data = Donation.objects.get(user=request.user, id=id) # ganti jd ambil data user buat cek wallet
#     return HttpResponse(serializers.serialize("json", donation_data), content_type="application/json")


