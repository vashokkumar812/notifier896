from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/(?P<room_name>\w+)/$', consumers.ChatConsumer),
    re_path(r'ws/not/(?P<room_name>\w+)/$', consumers.notConsumer),
]