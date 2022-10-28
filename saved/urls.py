from django.urls import path
from saved.views import show_saved, show_json

app_name = "saved"
urlpatterns = [
    path("<str:username>/", show_saved, name="show_saved"),
    path("json/<str:username>/", show_json, name="show_json"),
]
