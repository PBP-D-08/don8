from django.shortcuts import render
from homepage.models import Donation
from authentication.models import User
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from donation_app.forms import DonationForm
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
@login_required(login_url="/auth/login/")
def show_donation_page(request, id):
    context = {
        "form": DonationForm()
    }
    return render(request, "donation_page.html", context)

# fungsi buat update wallet user dan cek apakah mencukupi atau tidak
def make_donation(request, id):
    form = DonationForm(request.POST or None)
    if request.POST and form.is_valid():
        data = form.save(request, id) # form.save() return data
        return JsonResponse(data)


def show_json(request):
    donations = Donation.objects.all()
    return HttpResponse(
        serializers.serialize("json", donations), content_type="application/json"
    )

# mengambil data donasi dalam json by id
def get_donation_data(request, id):
    donation_data = Donation.objects.filter(id=id) # ganti jd ambil data user buat cek wallet
    return HttpResponse(serializers.serialize("json", donation_data), content_type="application/json")

def get_organization_data(request, id):
    organization_data = User.objects.filter(id=id)
    return HttpResponse(serializers.serialize("json", organization_data), content_type="application/json")

def check_user(request):    
    if request.user.is_authenticated:
        if request.user.role == 1:

            return JsonResponse({"pengguna": True})
            
    return JsonResponse({"pengguna": False})

def get_current_date(request):

    return JsonResponse({"current_date": datetime.date.today()})
