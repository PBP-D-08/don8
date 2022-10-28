from datetime import datetime
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render
from homepage.models import Donation


# Create your views here.
def index(request):
    return render(request, "index.html")


def show_json(request):
    donations = Donation.objects.all()
    return HttpResponse(
        serializers.serialize("json", donations), content_type="application/json"
    )


def add_ajax_donation(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        print(title)
        description = request.POST.get("description")
        date_expired = request.POST.get("date_expired")
        image_url = request.POST.get("image_url")
        date_created = datetime.today()
        user = request.user
        money_needed = request.POST.get("money_needed")
        d = Donation.objects.create(
            user=user,
            title=title,
            description=description,
            date_created=date_created,
            date_expired=date_expired,
            image_url=image_url,
            money_needed=money_needed
        )
        d.save()
    return JsonResponse({"instance": "success"}, status=200)
