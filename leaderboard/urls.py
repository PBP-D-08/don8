from django.urls import path
from .views import show_leaderboard, show_json_sorted

app_name = "leaderboard"

urlpatterns = [
    path("", show_leaderboard, name="show_leaderboard"),
    path("show_json_sorted/", show_json_sorted, name="show_json_sorted"),
]
