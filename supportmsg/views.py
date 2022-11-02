from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from supportmsg.models import Post
from homepage.models import Donation
from supportmsg.forms import PostForm
from django.contrib.auth.decorators import login_required
import json
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.
@login_required(login_url="/auth/login/")
def show_support(request):
    form = PostForm()
    all_donation = Donation.objects.all()
    context = {
        'donations' : all_donation,
        'form' : form,
    }
    return render(request, 'support.html', context)

@login_required(login_url="/auth/login/")
def show_json(request):
    data_post = Post.objects.all()
    res = []
    for obj in data_post:
        # Cek apakah user sudah like atau belum
        if obj.likes.filter(pk=request.user.pk).exists():
            status = True
        else:
            status = False
        res.append(
            {
                "pk": obj.pk,
                "fields": {
                    # "author": obj.author,
                    "author_name": obj.author_name,
                    "donation_name": obj.donation_name,
                    "message": obj.message,
                    "date_created": obj.date_created,
                    # "likes": obj.likes,
                    "likes_count": obj.num_likes,
                    "like_status": status,
                },
            }
        )
    # Sort by like count
    res.sort(key=lambda count :count.get("fields").get("likes_count"),reverse=True)
    return HttpResponse(json.dumps(res, indent=1, cls=DjangoJSONEncoder),content_type="application/json")
    # return HttpResponse(serializers.serialize("json", data_post), content_type="application/json")

@login_required(login_url="/auth/login/")
def add_message(request):
    form = PostForm(request.POST)
    if request.method == "POST" and form.is_valid():
        post = Post(
            author=request.user,
            author_name=request.user.username,
            donation_name = request.POST["donation-name"],
            message=request.POST["message"],
        )
        post.save()
        return HttpResponse(serializers.serialize("json", [post]), content_type="application/json")
    return HttpResponse(content_type="application/json")

@login_required(login_url="/auth/login/")
def like_post(request):
    if request.method == "POST":
        id = request.POST.get("post_id")
        post = Post.objects.filter(pk=id)[0]
        if not post.likes.filter(pk=request.user.pk).exists():
            post.likes.add(request.user)
            post.save()
        else:
            post.likes.remove(request.user)
            post.save()

        return HttpResponse(serializers.serialize("json", [post]), content_type="application/json")

    return HttpResponse("Invalid", status_code=405)
