
from django.urls import path
from threechat.views import chat, room

urlpatterns = [
    path('chat/', chat, name='chat_index'),
    path('chat/<str:room_name>/', room, name="chat_room"),
]
