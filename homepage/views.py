from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from homepage.models import Donation
from django.core.serializers.json import DjangoJSONEncoder
import json


# Create your views here.
def index(request):
    return render(request, "index.html")


def show_json(request):
    donations = Donation.objects.all()
    donations_dict = []
    for d in donations:
        donations_dict.append(
            {
                "pk": d.pk,
                "fields": {
                    "title": d.title,
                    "description": d.description,
                    "date_expired": d.date_expired,
                    "image_url": d.image_url,
                    "date_created": d.date_created,
                    "money_needed": d.money_needed,
                    "money_accumulated": d.money_accumulated,
                    "is_saved": d.saved.filter(
                        user__username=request.user.username
                    ).exists(),
                    "curr_role": request.user.role
                    if request.user.is_authenticated
                    else None,
                },
            }
        )
    return HttpResponse(
        json.dumps(donations_dict, indent=1, cls=DjangoJSONEncoder),
        content_type="application/json",
    )


def add_ajax_donation(request):
    if request.method == "POST":
        title = request.POST.get("title")
        print("tile: ", title)
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
            money_needed=money_needed,
        )
        d.save()
        return JsonResponse(
            {
                "pk": d.pk,
                "fields": {
                    "title": d.title,
                    "description": d.description,
                    "date_expired": d.date_expired,
                    "image_url": d.image_url,
                    "date_created": d.date_created,
                    "money_needed": d.money_needed,
                    "money_accumulated": d.money_accumulated,
                    "is_saved": False,
                    "curr_role": request.user.role,
                },
            },
            status=200,
        )
