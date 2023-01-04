
import os
# from django.conf.urls import url

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import app_test_ws.urls
import app_sp_operator.urls

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),

    'websocket': AuthMiddlewareStack(
        URLRouter(
            app_test_ws.urls.websocket_urlpatterns +
            app_sp_operator.urls.websocket_urlpatterns 
        )
    ),

})
