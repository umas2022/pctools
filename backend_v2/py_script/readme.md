# python功能拆分

### 安装必备库
- 参见 ./utils_env_init/setup.py

### 文件说明
- index.json: electron读取的功能目录,由py_server/app_sp_operator/views/SearcherFunction/list_update根据每个sp_xxx/intf.json生成

- set_xxx文件夹: 预设动作集,链式执行多个sp动作

- sp_xxx文件夹: 通过electron调用的批处理函数
    - xxx.py: 主功能函数,输入参数应包含json_set模式
        - 主类中应包含run()函数,作为后端调用的入口
    - usage.py: 功能测试函数,可以直接运行
    - intf.json: electron页面参数
        - 目前支持的类型:[input,select,switch,button]
        - 支持使用show字段控制显示,参见remove_keyword
        - switch参见sp_remove_keyword
        - button参见sp_crawler_bookwalker
        - annotation注释支持字符串和数组两种格式
    - __init__.py: 将功能涉及的类统一重命名,主类命名为MainClass,供django统一调用
    
- utils_xxx文件夹: 内部调用的辅助函数
