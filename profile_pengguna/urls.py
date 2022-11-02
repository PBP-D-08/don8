from django.urls import path
from profile_pengguna.views import *

app_name = "profile/user"

urlpatterns = [
    path("<str:username>/", profile_pengguna, name="profile_pengguna"),
    path("<str:username>/history/", show_donated, name="show_donated"),
    path("<str:username>/history/json/", show_json_history, name="show_json_history"),
    path("<str:username>/topup/", show_json_balance, name="show_json_balance"),
    
]