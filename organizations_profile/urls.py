from django.urls import path
from organizations_profile.views import organizations_profile, show_json

app_name = "org"

urlpatterns = [
    path("<str:id>/", organizations_profile, name="organizations_profile"),
    path("show_json/", show_json, name="show_json"),
]
