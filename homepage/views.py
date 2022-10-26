from urllib import response
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from homepage.models import Donation


# Create your views here.
def index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("decription")
        date_expired = request.POST.get("date_expired")
        image_url = request.POST.get("image_url")

    return render(request, "index.html")


def show_json(request):
    donations = Donation.objects.all()
    return HttpResponse(
        serializers.serialize("json", donations), content_type="application/json"
    )
