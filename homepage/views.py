from urllib import response
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("decription")
        date_expired = request.POST.get("date_expired")
        image_url = request.POST.get("image_url")

    return render(request, 'index.html')