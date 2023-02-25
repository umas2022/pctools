# 从0开始的django项目搭建

### info
- 2023.2.25
- Django version 4.1.7
- ASGI/Daphne version 4.0.0

### 创建项目
```
django-admin.exe startproject pj_test
```

### 启动项目  
```
python manage.py migrate
python ./manage.py runserver 0.0.0.0:4090
``` 

### 添加http应用

- 添加app
```
python manage.py startapp hello_umas
```

- app添加views: hello_umas/views.py
```python
from django.http import HttpResponse
def hello_umas(request):
    '''basic response test'''
    print("request:")
    print(request.body)
    return HttpResponse("test Hello world ")
```

- app添加urls: hello_umas/urls.py
```python
from django.urls import path
from . import views
urlpatterns = [
    path("hello_umas",views.hello_umas),
]
```

- 全局添加urls: pj_test/urls.py
```python
from django.conf.urls import include
urlpatterns = [
    path(r'',include("hello_umas.urls"))
]
```

### 添加websocket应用
- 参考：[channels官方文档](https://channels.readthedocs.io/en/stable/tutorial/part_1.html)

- 安装必备库
```python
pip install channels
pip install daphne
```

- 添加设置: pj_test/settings.py,注意daphne要写在最上面,这一步配置完毕后启动服务器可以看到ASGI/Daphne版本号
```python
INSTALLED_APPS = [
    'daphne',
    'hello_ws',
    '...',
]
ASGI_APPLICATION = 'pj_test.asgi.application'
```

- 创建app
```
python manage.py startapp hello_ws
```

- app添加views: hello_ws/views.py
```python
from channels.generic.websocket import WebsocketConsumer
class WebsocketTest(WebsocketConsumer):
    '''websocket test'''
    def connect(self):
        self.accept()
    def disconnect(self, close_code):
        pass
    def receive(self, text_data):
        print(text_data)
        for i in range(10):
            self.send(str(i))
```

- app添加urls: hello_ws/urls.py
```python
from django.urls import path
from . import views
websocket_urlpatterns = [path("hello_ws",views.WebsocketTest.as_asgi())]
```

- 全局添加asgi: pj_test/asgi.py
```python
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pj_test.settings")
django_asgi_app = get_asgi_application()

import hello_ws.urls

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(URLRouter(
        hello_ws.urls.websocket_urlpatterns
    ))
})
```

### 可能出现的问题
- websocket 403
    - 禁用crsf或者设置允许所有请求,方法很多,不再赘述

- Cannot import ASGI_APPLICATION module
    - 启用shell调试模式
    ```python manage.py shell```
    ```from py_server.asgi import application```