from django.urls import path
from donation_app.views import show_donation_page, make_donation, show_json, get_donation_data, get_organization, check_user, get_current_date, get_last_donation, flutter_make_donation, flutter_donation_creator

app_name = 'donation_app'

urlpatterns = [
    path('<int:id>/', show_donation_page, name='show_donation_page'),
    path('make-donation/<int:id>/', make_donation, name='make_donation'),
    path('', show_json, name='show_json'),
    path('json-donation/<int:id>/', get_donation_data, name='get_donation_data'),
    path('json-organization/<int:id>/', get_organization, name='get_organization'),
    path('check-user/', check_user, name='check_user'),
    path('get-current-date/', get_current_date, name='get_current_date'),
    path('get-last-donation/<int:id>/', get_last_donation, name='get_last_donation'),
    path('flutter-make-donation/', flutter_make_donation, name='flutter_make_donation'),
    path('flutter-donation-creator/<int:id>/', flutter_donation_creator, name = "flutter_donation_creator"),
]