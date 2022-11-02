from django.http import HttpResponse
from django.shortcuts import render
from homepage.models import Donation
from django.core import serializers

# Create your views here.
def show_leaderboard(request):
    return render(request, "leaderboard.html")

def show_json_sorted(request):
    donations = Donation.objects.all().order_by('-money_accumulated').only()
    return HttpResponse(serializers.serialize('json', donations), content_type='application/json')
