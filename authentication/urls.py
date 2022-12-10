from django.urls import path
from authentication.views import (
    login_role,
    register,
    logout_role,
    check_login,
    login_role_flutter,
    logout_role_flutter,
    register_flutter,
)

app_name = "auth"

urlpatterns = [
    path("login/", login_role, name="login"),
    path("login_flutter/", login_role_flutter, name="login_flutter"),
    path("register/", register, name="register"),
    path("register_flutter/", register_flutter, name="register_flutter"),
    path("logout/", logout_role, name="logout"),
    path("logout_flutter/", logout_role_flutter, name="logout_flutter"),
    path("check_login/", check_login, name="check_login"),
]
