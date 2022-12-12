from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from authentication.models import User
from homepage.models import Donation
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request, "index.html")


@login_required(login_url="/auth/login/")
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


@csrf_exempt
def add_ajax_donation_mobile(request):
    if request.method == "POST":
        title = request.POST.get("title")
        print("tile: ", title)
        description = request.POST.get("description")
        date_expired_string = request.POST.get("date_expired")
        image_url = request.POST.get("image_url")
        date_created = datetime.today()
        # user = request.user
        # datetime_str = '09/19/18 13:55:26

        date_expired = datetime.strptime(
            date_expired_string, '%Y-%m-%d')

        money_needed = request.POST.get("money_needed")
        user_id = int(request.POST.get("user_id"))
        user = User.objects.get(id=user_id)

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
                    "curr_role": d.user.role,
                },
                "success": True,

            },
            status=200,
        )
