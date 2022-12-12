from django.urls import path
from profile_pengguna.views import *

app_name = "profile/user"

urlpatterns = [
    path("<str:username>/", profile_pengguna, name="profile_pengguna"),
    path("<str:username>/history/", show_donated, name="show_donated"),
    path("<str:username>/history/json/", show_json_history, name="show_json_history"),
    path("<str:username>/topup/", show_json_balance, name="show_json_balance"),
    path("<str:username>/amount/", show_json_amount, name="show_json_amount"),
    path("<str:username>/flutter-history/", flutter_history, name="flutter_history"),
    path("<str:username>/flutter-top-up/", flutter_top_up, name="flutter_top_up"),
    
]