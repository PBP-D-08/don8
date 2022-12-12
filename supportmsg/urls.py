from django.urls import path
from supportmsg.views import show_support
from supportmsg.views import show_json
from supportmsg.views import add_message
from supportmsg.views import add_message_flutter
from supportmsg.views import like_post
from supportmsg.views import like_post_flutter

app_name = 'supportmsg'

urlpatterns = [
    path('', show_support, name='show_support'),
    path('json/<str:filter>/', show_json, name='show_json'),
    path('add-message/', add_message, name="add_message"),
    path('add-message-flutter/', add_message_flutter, name="add_message_flutter"),
    path('like-post/', like_post, name="like_post"),
    path('like-post-flutter/', like_post_flutter, name="like_post_flutter"),
]