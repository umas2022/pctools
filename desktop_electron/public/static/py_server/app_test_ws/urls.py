from django.urls import path
from . import views

urlpatterns =[]

websocket_urlpatterns = [
    path("app_test_ws",views.WebsocketTest.as_asgi())
]