from django.urls import path
from saved.views import create_saved, show_saved, show_json, delete_saved

app_name = "saved"
urlpatterns = [
    path("", create_saved, name="create_saved"),
    path("delete/<int:donation_id>", delete_saved, name="delete_saved"),
    path("<str:username>/", show_saved, name="show_saved"),
    path("json/<str:username>/", show_json, name="show_json"),
]
