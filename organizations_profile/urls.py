from django.urls import path
from organizations_profile.views import organizations_profile, show_json, show_jsoncomp, show_jsonexp, show_jsonpro

app_name = "profile/org"

urlpatterns = [
    path("<str:id>/", organizations_profile, name="organizations_profile"),
    path("<str:id>/donations/", show_json, name="show_json"),
    path("<str:id>/donationscomp/", show_jsoncomp, name="show_json"),
    path("<str:id>/donationsexp/", show_jsonexp, name="show_json"),
    path("<str:id>/donationspro/", show_jsonpro, name="show_json"),
]
