from django.urls import path
from .consumers import PLCConsumer

websocket_urlpatterns = [
    path("ws/plc/", PLCConsumer.as_asgi()),
]