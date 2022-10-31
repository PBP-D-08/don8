from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from homepage.models import Donation
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import json

# Create your views here.
def show_leaderboard(request):
    return render(request, "leaderboard.html")

def show_json_sorted(request):
    donations = Donation.objects.all().order_by('-money_accumulated').only()
    return HttpResponse(serializers.serialize('json', donations), content_type='application/json')
