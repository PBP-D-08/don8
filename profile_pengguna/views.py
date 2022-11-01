from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from profile_pengguna.models import Profile
from django.core.serializers.json import DjangoJSONEncoder
import json
from authentication.models import User
from profile_pengguna.forms import Form
from donation_app.models import UserDonation
from django.core import serializers

# Create your views here.
@login_required(login_url="/auth/login/")
def profile_pengguna(request, username):
    if request.user.username != username and request.user.role != User.USER:
        return HttpResponse("You are not authorized to view this page.")

    profiles = list(User.objects.filter(username=username))
    for i in profiles:
        userp = i
        
    donations = list(UserDonation.objects.filter(user=userp))
    money_donated = 0
    for d in donations:
        money_donated += d.amount_of_donation

    profile = Profile.objects.get(user=userp)
    profile.money_donated = money_donated
    
    profile.save()

    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            profile.user.balance += form.cleaned_data["amount"]
            profile.user.save()
            context = {
                "username": profile.user.username,
                "money_donated": profile.money_donated,
                "balance": profile.user.balance
            }
            return JsonResponse(context)
    else:
        form = Form()

    context = {
                "username": profile.user.username,
                "money_donated": profile.money_donated,
                "balance": profile.user.balance,
                'form': form,
            }
        
    return render(request, "user_profile.html", context)

@login_required(login_url="/auth/login/")
def show_donated(request, username):
    if request.user.username != username and request.user.role != User.USER:
        return HttpResponse("You are not authorized to view this page.")
    return render(request, "history.html")

@login_required(login_url="/auth/login/")
def show_json_history(request, username):
    if request.user.username != username and request.user.role != User.USER:
        return HttpResponse("You are not authorized to view this page.")
    
    profile = UserDonation.objects.filter(user=request.user)
    history = [h for h in profile]
    history_dict = []
    for h in history:
        history_dict.append(
            {
                "pk": h.pk,
                "fields": {
                    "title": h.donation.title,
                    "image_url": h.donation.image_url,
                    "donation": h.donation.pk,
                    "date": h.date,
                    "amount": h.amount_of_donation
                },
            }
        )
    return HttpResponse(
        json.dumps(history_dict, indent=1, cls=DjangoJSONEncoder),
        content_type="application/json",
    )

def show_json_balance(request, username):
    return HttpResponse(serializers.serialize("json", User.objects.filter(username=username)), content_type="application/json")