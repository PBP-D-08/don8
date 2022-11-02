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
    org_profile = Profile.objects.get(organization=profile)
    donations = Donation.objects.filter(user=profile)
    for i in donations:
        i.org_name = profile.username
        i.save()
    org_profile.total_campaign = len(donations)
    org_profile.save()

    if request.method == "POST":
        form = WithdrawForm(request.POST)
        if form.is_valid():
            if (org_profile.withdrawn + form.cleaned_data["amount"]) <= profile.balance:
                org_profile.withdrawn += form.cleaned_data["amount"]
                org_profile.save()
                context = {
                    "profile_b": profile.balance, "profile_w": org_profile.withdrawn, "profile_t": org_profile.total_campaign,
                }
                return JsonResponse(context)
            else:
                context = {
                    "profile_b": profile.balance, "profile_w": org_profile.withdrawn, "profile_t": org_profile.total_campaign,
                }
                return JsonResponse(context)
    else:
        form = WithdrawForm()
    context = {
        'nama': id,
        'profile': profile,
        'form': form,
        'org_profile': org_profile,
        'user': request.user,
    }
    return render(request, "profile.html", context)


def show_json(request, id):
    profile = list(User.objects.filter(username=id))
    for i in profile:
        profile = i
    org_profile = Profile.objects.get(organization=profile)
    donations = Donation.objects.filter(user=profile)

    return HttpResponse(
        serializers.serialize("json", donations), content_type="application/json"
    )

def show_jsoncomp(request, id):
    profile = list(User.objects.filter(username=id))
    for i in profile:
        profile = i
    org_profile = Profile.objects.get(organization=profile)
    donation = Donation.objects.filter(user=profile)
    donations = []
    for i in donation:
        if i.money_accumulated >= i.money_needed:
            donations.append(i)


    return HttpResponse(
        serializers.serialize("json", donations), content_type="application/json"
    )

def show_jsonexp(request, id):
    profile = list(User.objects.filter(username=id))
    for i in profile:
        profile = i
    org_profile = Profile.objects.get(organization=profile)
    donation = Donation.objects.filter(user=profile)
    donations =[]
    for i in donation:
        if i.date_expired < datetime.now().date():
            donations.append(i)

    return HttpResponse(
        serializers.serialize("json", donations), content_type="application/json"
    )

def show_jsonpro(request, id):
    profile = list(User.objects.filter(username=id))
    for i in profile:
        profile = i
    org_profile = Profile.objects.get(organization=profile)
    donation = Donation.objects.filter(user=profile)
    donations = []
    for i in donation:
        if i.date_expired > datetime.now().date():
            donations.append(i)

    return HttpResponse(
        serializers.serialize("json", donations), content_type="application/json"
    )