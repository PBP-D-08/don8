from django.http import HttpResponse
from django.shortcuts import render
from authentication.views import login_role
from saved.models import SavedDonation
from django.core import serializers
from django.contrib.auth.decorators import login_required
from authentication.models import User

# Create your views here.
@login_required(login_url="/login/")
def show_saved(request, username):
    if request.user.username != username and not request.user.role != User.USER:
        return HttpResponse("You are not authorized to view this page.")
    return render(request, "saved.html")


@login_required(login_url="/login/")
def show_json(request, username):
    if request.user.username != username and not request.user.role != User.USER:
        return HttpResponse("You are not authorized to view this page.")
    saved_donations = SavedDonation.objects.filter(user__username=username)
    donations = [sd.donation for sd in saved_donations]
    data = serializers.serialize("json", donations)
    return HttpResponse(
        serializers.serialize("json", donations), content_type="application/json"
    )
