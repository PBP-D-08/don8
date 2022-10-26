from django.urls import path
from homepage.views import index, show_json

app_name = "homepage"

urlpatterns = [
    path("", index, name="index"),
    path("donation/", show_json, name="show_json"),
]
