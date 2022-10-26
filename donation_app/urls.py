from django.urls import path
from donation_app.views import show_donation_page, make_donation, update_money_accumulated, get_donation_data

app = 'donation_app'

urlpatterns = [
    path('/<int:id>', show_donation_page, name='show_donation_page'),
    path('make-donation/<int:id>', make_donation, name='make_donation'),
    path('update-money-accumulated/<int:id>', update_money_accumulated, name='update_money_accumulated')
    # path('json/<int:id>', get_donation_data, name='get_donation_data'),
]