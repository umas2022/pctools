from django.urls import path
from . import views

urlpatterns = [
    path("app_test",views.app_test),
]

# websocket_urlpatterns = [
#     path("app_test_ws",views.AppTestWS.as_asgi()),
# ]