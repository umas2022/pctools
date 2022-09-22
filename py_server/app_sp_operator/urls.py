from django.urls import path
from . import views

urlpatterns =[]

websocket_urlpatterns = [
    path("sp_operator",views.SpOperator.as_asgi())
]