from django.urls import re_path
from threechat.consumers import RoomConsumer

ws_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', RoomConsumer.as_asgi())
]