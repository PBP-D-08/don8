from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from homepage.models import Donation


# Create your views here.
def index(request):
    return render(request, "index.html")


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
