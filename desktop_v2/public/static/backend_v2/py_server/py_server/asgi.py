
import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'py_server.settings')

import app_test_ws.urls
import app_sp_operator.urls


application = ProtocolTypeRouter({
    "http": get_asgi_application(),

    'websocket': AuthMiddlewareStack(
        URLRouter(
            app_test_ws.urls.websocket_urlpatterns +
            app_sp_operator.urls.websocket_urlpatterns 
        )
    ),

})
