from django.urls import path
from homepage.views import index, show_json,add_ajax_donation

app_name = "homepage"

urlpatterns = [
    path("", index, name="index"),
    path("donation/", show_json, name="show_json"),
    path('add_ajax_donation/', add_ajax_donation, name='add_ajax_donation')
]
