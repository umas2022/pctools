from django.urls import path
from . import views

urlpatterns =[]

websocket_urlpatterns = [
    path("sp_searcher",views.SpSearcher.as_asgi())
]