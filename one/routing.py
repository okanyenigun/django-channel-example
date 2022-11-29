from django.urls import path
from one.consumers import OneConsumer

ws_urlpatterns = [
    path('ws/any_url/', OneConsumer.as_asgi())
]