from django.urls import path
from supportmsg.views import show_support
from supportmsg.views import show_json
from supportmsg.views import add_message
from supportmsg.views import like_post

app_name = 'supportmsg'

urlpatterns = [
    path('', show_support, name='show_support'),
    path('json/<str:filter>/', show_json, name='show_json'),
    path('add-message/', add_message, name="add_message"),
    path('like-post/', like_post, name="like_post"),
]