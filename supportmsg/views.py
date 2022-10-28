from django.shortcuts import render
from urllib import response
from django.http import HttpResponse
from django.core import serializers
from supportmsg.models import Post

# Create your views here.
def show_support(request):
    return render(request, 'support.html')

def show_json(request):
    data_post = Post.objects.all()
    return HttpResponse(serializers.serialize("json", data_post), content_type="application/json")

def add_message(request):
    if request.method == "POST":
        post = Post(
            author=request.user,
            author_name=request.user.username,
            message=request.POST["message"],
        )
        post.save()
        return HttpResponse(serializers.serialize("json", [post]), content_type="application/json")

    return HttpResponse("Invalid", status_code=405)