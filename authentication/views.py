from django.shortcuts import render, redirect
from authentication.models import User
from organizations_profile.models import ProfileO
from profile_pengguna.models import ProfileU
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from authentication.forms import RegisterForm
import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        print(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            role = form.cleaned_data.get("role")
            user = User.objects.create_user(
                username=username,
                password=password,
                role=User.USER if role == "user" else User.COMPANY,
            )
            if user.role == User.COMPANY:
                profile = ProfileO.objects.create(organization=user)
                profile.save()
            elif user.role == User.USER:
                profile = ProfileU.objects.create(user=user)
                profile.save()
            messages.success(request, "Akun berhasil dibuat")
            return redirect("auth:login")
        else:
            messages.error(request, form.errors)
    return render(request, "register.html", {"form": form})


@csrf_exempt
def register_flutter(request):
    form = RegisterForm()
    if request.method == "POST":
        print(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            role = form.cleaned_data.get("role")
            user = User.objects.create_user(
                username=username,
                password=password,
                role=User.USER if role == "user" else User.COMPANY,
            )
            if user.role == User.COMPANY:
                profile = ProfileO.objects.create(organization=user)
                profile.save()
            elif user.role == User.USER:
                profile = ProfileU.objects.create(user=user)
                profile.save()
            return JsonResponse(
                {
                    "status": True,
                    "message": "User successfully registered",
                },
                status=200,
            )
        else:
            return JsonResponse(
                {
                    "status": False,
                    "message": "Something went wrong",
                },
                status=400,
            )
    return render(request, "register.html", {"form": form})


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


@csrf_exempt
def login_role_flutter(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse(
                {
                    "status": True,
                    "message": "Successfully Logged In!",
                    "user_data": {
                        "id": user.id,
                        "username": username,
                        "role": 3 if request.user.is_superuser else user.role,
                        "balance": user.balance,
                    },
                },
                status=200,
            )
        else:
            messages.info(request, "Username atau password salah")
            return JsonResponse(
                {
                    "status": False,
                    "message": "Failed to Login, Account Disabled.",
                },
                status=401,
            )
    return render(request, "login.html")


def logout_role(request):
    logout(request)
    response = HttpResponseRedirect(reverse("homepage:index"))
    response.delete_cookie("last_login")
    return response


@csrf_exempt
def logout_role_flutter(request):
    logout(request)
    return JsonResponse(
        {"status": True, "message": "Successfully logged out"}, status=200
    )


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
