from django.urls import path
from supportmsg.views import show_support
from supportmsg.views import show_json
from supportmsg.views import add_message

app_name = 'supportmsg'

urlpatterns = [
    path('', show_support, name='show_support'),
    path('json/', show_json, name='show_json'),
    path('add-message/', add_message, name="show_json"),
]