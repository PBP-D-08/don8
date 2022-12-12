from django.urls import path
from homepage.views import index, add_ajax_donation, add_ajax_donation_mobile

app_name = "homepage"

urlpatterns = [
    path("", index, name="index"),
    path("add_ajax_donation/", add_ajax_donation, name="add_ajax_donation"),
    path("add_ajax_donation_mobile/", add_ajax_donation_mobile,
         name="add_ajax_donation_mobile"),
]
