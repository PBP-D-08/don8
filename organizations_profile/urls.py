from django.urls import path
from organizations_profile.views import organizations_profile, show_json, show_jsoncomp, show_jsonexp, show_jsonpro, \
    show_jsonf, show_jsoncompf, show_jsonexpf, show_jsonprof, post_orgproff, show_orgproff

app_name = "profile/org"

urlpatterns = [
    path("<str:id>/", organizations_profile, name="organizations_profile"),
    path("<str:id>/donations/", show_json, name="show_json"),
    path("<str:id>/donationscomp/", show_jsoncomp, name="show_json"),
    path("<str:id>/donationsexp/", show_jsonexp, name="show_json"),
    path("<str:id>/donationspro/", show_jsonpro, name="show_json"),
    path("<str:id>/donationsf/", show_jsonf, name="show_json"),
    path("<str:id>/donationscompf/", show_jsoncompf, name="show_json"),
    path("<str:id>/donationsexpf/", show_jsonexpf, name="show_json"),
    path("<str:id>/donationsprof/", show_jsonprof, name="show_json"),
    path("<str:id>/donationsshow/", show_orgproff, name="show_json"),
    path("<str:id>/donationspost/", post_orgproff, name="show_json"),
]
