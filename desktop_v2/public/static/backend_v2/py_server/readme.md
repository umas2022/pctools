# 后端readme

## 文件目录结构
- app_sp_operator [工具箱相关api]
- app_test [测试代码]
- app_test_ws [demo:websocket模板]
- py_server [django主app]
- templates
- utils [自建工具]


## 使用说明
- 手动启动服务器（backend文件夹下）  
    ```python ./manage.py runserver 0.0.0.0:8008```  
    网页访问：http://localhost:8008/


- 应用迁移
    ```python manage.py migrate```
    - 一般需要用的时候会红字报警的, 不用刻意调
    
- 启用shell调试
    ```python manage.py shell```
    - 例如可以from py_server.asgi import application查看报错在哪里

