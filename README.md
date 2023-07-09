# python批处理工具箱（电脑配件）


## 简介
- python写的批处理脚本越来越多，就想着能不能做一个ui
- 因为技能树限制，采用electron -> django -> python脚本


## 功能
(./py_script/index.json)
- 预设
  - copy动作集
  - 全接口demo
- 自动化
  - 点击 - 连续点击
  - 远程 - 执行命令
  - 识别 - 窗口截图
  - 识别 - 静态检测
  - 识别 - 截图翻译
- 压缩
  - 压缩 - 打包7z
- 拷贝
  - 拷贝 - 筛选拷贝
  - 拷贝 - 拷贝合并
  - 拷贝 - 图片压缩
  - 拷贝 - 视频压缩
  - 拷贝 - 幻影坦克
  - 拷贝 - 拷贝拆分
  - 拷贝 - mp4转gif
  - 拷贝 - wsa文件复制
- 爬虫
  - 爬虫 - bookwalker通用
- 删除
  - 删除 - 删除差异
  - 删除 - 图片查重
  - 删除 - 删除关键字
- 重命名
  - 重命名 - 基本方法合集
- 搜索
  - 搜索 - 所有后缀

## Introduction
- python basic function (py_script/)
- Django backend server (py_server/)
- Electron+Vue frontend (desktop_electron/)
- pyqt6 desktup (desktop_pyqt/) (已经放弃更新)
- 没有传release,感兴趣可以微信找我(umas)

## Environment
参见 [./0-docs/deploy.md](https://github.com/umas2022/pctools/blob/main/0-docs/deploy.md)


## 初次部署
- 设置页输入环境安装路径，点击py环境初始化按钮（注意环境安装路径输入后要点击修改按钮）
- 如果按钮没反应,手动运行/py_script/utils_env_init/setup.py
- 项目部署将会创建venv虚拟环境并在其中安装必备运行库


## 开发者功能
- 开启开发模式服务器

```bash
python run_electron.py
```

- 打包

```bash
python build_electron.py
```

- 新功能在./py_script/添加，注意目录结构格式
- 如果有新模组需要pip安装，写在./py_script/utils_env_init/pip_requirements.txt，然后在前端的设置页里点击【python环境初始化】按钮。（按钮可能会因为权限问题报错，手动运行./py_script/utils_env_init/setup_venv.py，注意设置安装目录）



