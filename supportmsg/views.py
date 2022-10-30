from django.shortcuts import render
from urllib import response
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from supportmsg.models import Post
from homepage.models import Donation
from supportmsg.forms import PostForm
import json


# Create your views here.
def show_support(request):
    form = PostForm()
    all_donation = Donation.objects.all()
    context = {
        'donations' : all_donation,
        'form' : form
    }
    return render(request, 'support.html', context)

def show_json(request):
    data_post = Post.objects.all()
    # tes = Post.objects.filter(author__username = "akunbaru")
    return HttpResponse(serializers.serialize("json", data_post), content_type="application/json")

def add_message(request):
    if request.method == "POST":
        post = Post(
            author=request.user,
            author_name=request.user.username,
            donation_name = request.POST["donation_name"],
            message=request.POST["message"],
        )
        post.save()
        return HttpResponse(serializers.serialize("json", [post]), content_type="application/json")

    return HttpResponse("Invalid", status_code=405)

def like_post(request):
    if request.method == "POST":
        id = request.POST.get("post_id")
        # print(id)
        post = Post.objects.filter(pk=id)[0]
        # print(post)
        if not post.likes.filter(pk=request.user.pk).exists():
            post.likes.add(request.user)
            post.save()
        else:
            post.likes.remove(request.user)
            post.save()

        return HttpResponse(serializers.serialize("json", [post]), content_type="application/json")

    return HttpResponse("Invalid", status_code=405)
