from datetime import datetime
from urllib import response
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from homepage.models import Donation


# Create your views here.
def organizations_profile(request, id):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        date_expired = request.POST.get("date_expired")
        image_url = request.POST.get("image_url")
        date_created = datetime.now()
        user = request.user
        Donation.objects.create(
            user=user,
            title=title,
            description=description,
            date_created=date_created,
            date_expired=date_expired,
            image_url=image_url,
        )
    return render(request, "profile.html")


def show_json(request):
    donations = Donation.objects.all()
    return HttpResponse(
        serializers.serialize("json", donations), content_type="application/json"
    )
