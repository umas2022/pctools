# 后端readme

## 文件目录结构（已弃懒改）
- app_backup [备份相关api]
- app_rename [重命名相关api]
- app_test [测试代码]
- app_test_ws [demo:websocket模板]
- interface [django主app]
- templates
- utils [自建工具]


## 使用说明
- 手动启动服务器（backend文件夹下）  
    ```python ./manage.py runserver 0.0.0.0:8008```  
    网页访问：http://localhost:8008/

- 新建app  
    ```python manage.py startapp app_test```
    - py_server/settings.py中INSTALLED_APPS注册app
    - 添加views.py, urls.py
    - py_server/asgi.py中添加url（websocket）

- 新建websocket app
    ```python manage.py startapp app_test_ws```
    - 添加views: app_test_ws/views.py
    ```python
    from channels.generic.websocket import WebsocketConsumer
    class WebsocketTest(WebsocketConsumer):
        '''websocket test'''
        def connect(self):
            self.accept()
        def disconnect(self, close_code):
            pass
        def receive(self, text_data):
            pass
    ```
    - 添加url: app_test_ws/urls.py
    ```python
    from django.urls import path
    from . import views
    websocket_urlpatterns = [path("app_test_ws",views.WebsocketTest.as_asgi())]
    ```
    - 添加asgi: py_server/asgi.py
        - URLRouter本质是字符串，新增的url用+连接即可
    ```python
    import app_test_ws.urls
    application = ProtocolTypeRouter({
        "http": get_asgi_application(),
        'websocket': AuthMiddlewareStack(
            URLRouter(app_test_ws.urls.websocket_urlpatterns + xxx)
        ),
    })
    ```

- 应用迁移
    ```python manage.py migrate```
    - 一般需要用的时候会红字报警的，不用刻意调
    
- 启用shell调试
    ```python manage.py shell```
    - 例如可以from py_server.asgi import application查看报错在哪里

