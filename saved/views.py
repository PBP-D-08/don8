from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from saved.models import SavedDonation
from django.contrib.auth.decorators import login_required
from authentication.models import User
from django.core.serializers.json import DjangoJSONEncoder
import json

# Create your views here.
@login_required(login_url="/auth/login/")
def show_saved(request, username):
    if request.user.username != username and request.user.role != User.USER:
        return HttpResponse("You are not authorized to view this page.")
    return render(request, "saved.html")


@login_required(login_url="/auth/login/")
def show_json(request, username):
    if request.user.username != username and request.user.role != User.USER:
        return HttpResponse("You are not authorized to view this page.")
    saved_donations = SavedDonation.objects.filter(user__username=username)
    donations = [sd.donation for sd in saved_donations]
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
                    "is_saved": True,
                    "curr_role": request.user.role,
                },
            }
        )
    return HttpResponse(
        json.dumps(donations_dict, indent=1, cls=DjangoJSONEncoder),
        content_type="application/json",
    )


@login_required(login_url="/auth/login/")
def create_saved(request):
    if request.user.role != User.USER:
        return HttpResponse("You are not authorized to post.")
    if request.method == "POST":
        user = request.user
        donation_id = request.POST.get("id")
        if SavedDonation.objects.filter(user=user, donation__pk=donation_id).exists():
            return JsonResponse({"status": 409})
        SavedDonation.objects.create(user=user, donation_id=donation_id)
        return JsonResponse({"status": 200})
    return HttpResponse("This page is not available.")


@login_required(login_url="/auth/login/")
def delete_saved(request, donation_id):
    if request.user.role != User.USER:
        return HttpResponse("You are not authorized to delete.")
    if request.method == "DELETE":
        user = request.user
        if SavedDonation.objects.filter(user=user, donation__pk=donation_id).exists():
            sd = SavedDonation.objects.get(user=user, donation__pk=donation_id)
            sd.delete()
            return JsonResponse({"status": 200})
        return JsonResponse({"status": 404})
    return HttpResponse("This page is not available.")
