from datetime import datetime
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render
from homepage.models import Donation
from organizations_profile.models import Profile
from authentication.models import User
from organizations_profile.forms import WithdrawForm



# Create your views here.
def organizations_profile(request, id):
    profiles = list(User.objects.filter(username=id))
    for i in profiles:
        profile = i
    if request.method == "POST":
        form = WithdrawForm(request.POST)
        if form.is_valid():
            profile.balance -= form.cleaned_data["amount"]
            profile.save()
            context = {
                "profile": profile.balance,
            }
            return JsonResponse(context)
    else:
        form = WithdrawForm()
    context = {
        'nama': id,
        'profile': profile,
        'form': form,
    }
    return render(request, "profile.html", context)


def show_json(request, id):
    profile = list(User.objects.filter(username=id))
    for i in profile:
        profile = i
    donations = Donation.objects.filter(user=profile)
    for i in donations:
        i.org_name = profile.username
        i.save()
    profile.total_campaign = len(donations)
    profile.save()

    return HttpResponse(
        serializers.serialize("json", donations), content_type="application/json"
    )