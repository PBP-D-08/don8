from django.urls import path
from supportmsg.views import show_support
app_name = 'supportmsg'

urlpatterns = [
    path('', show_support, name='show_support'),
]