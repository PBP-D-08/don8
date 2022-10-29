from django.urls import path
from donation_app.views import show_donation_page, make_donation, show_json, get_donation_data, check_user

app_name = 'donation_app'

urlpatterns = [
    path('<int:id>/', show_donation_page, name='show_donation_page'),
    path('make-donation/<int:id>/', make_donation, name='make_donation'),
    path('', show_json, name='show_json'),
    path('json/<int:id>/', get_donation_data, name='get_donation_data'),
    path('check-user/', check_user, name="check_user")
]