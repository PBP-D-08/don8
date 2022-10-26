from django.shortcuts import render, redirect
from authentication.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        role = request.POST.get("role")
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists")
        elif password1 == password2:
            user = User.objects.create_user(username=username, password=password1)
            user.role = User.USER if role == "user" else User.COMPANY
            user.save()
            messages.success(request, "Akun berhasil dibuat")
            return redirect("auth:login")
        else:
            messages.info(request, "Password tidak sama")
    return render(request, "register.html")


def login_role(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(
                reverse("homepage:index")
            )  # membuat response
            response.set_cookie(
                "last_login", str(datetime.datetime.now())
            )  # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, "Username atau password salah")
    return render(request, "login.html")


def logout_role(request):
    logout(request)
    response = HttpResponseRedirect(reverse("homepage:index"))
    response.delete_cookie("last_login")
    return response


def check_login(request):
    # return in json
    return JsonResponse(
        {
            "is_login": request.user.is_authenticated,
            "role": request.user.role if request.user.is_authenticated else None,
            "username": request.user.username
            if request.user.is_authenticated
            else None,
        },
        status=200,
    )
