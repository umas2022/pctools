# 电脑配件后端打包

## 初始化运行环境
- setup.py

## 参数修改
- user_config.json

## 说明
- backend_v2文件夹被整个打包进electron,必须通过run_electron.py脚本拷贝后才能运行
- index.json的修改由前端触发,只会在electron的包中被修改,backend_v2外部文件夹中不会同步修改