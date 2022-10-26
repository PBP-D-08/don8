from django.urls import path
from authentication.views import login_role, register, logout_role, check_login

app_name = "auth"

urlpatterns = [
    path("login/", login_role, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout_role, name="logout"),
    path("check_login/", check_login, name="check_login"),
]
