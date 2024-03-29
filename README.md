# python批处理工具箱（电脑配件）






## Introduction
- python写的批处理脚本越来越多，做了一个ui统一调用
- 因为技能树限制，采用electron(vue) -> django -> python脚本
- 没有传release,感兴趣可以微信找我(umas)



## 界面

<img src="https://github.com/umas2022/pctools/blob/main/0-docs/img/example.jpg" width="60%" height="30%">



## 所有功能
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
  - 拷贝 - 图片压缩
  - 拷贝 - 视频压缩
  - 拷贝 - 拷贝合并
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
    - 添加前缀
    - 删除前缀
    - 关键字替换
    - 序号命名
- 搜索
  - 搜索 - 所有后缀


## Environment
参见 [./0-docs/deploy.md](https://github.com/umas2022/pctools/blob/main/0-docs/deploy.md)


## 初次部署
- 系统需要安装有python
- 设置页输入环境安装路径，点击py环境初始化按钮（注意环境安装路径输入后要点击修改按钮）
- 如果按钮没反应,手动运行/py_script/utils_env_init/setup.py
- 项目部署将会创建venv虚拟环境并在其中安装必备运行库


## 开发备忘

- 脚本：启动开发模式服务器

```bash
python run_electron.py
# 后端路径自动切换为开发路径
```

- 脚本：打包

```bash
python build_electron.py
# 打包路径：pctools\desktop_electron\dist_electron
```


- 新功能在./py_script/添加，注意目录结构格式，添加后运行build_electron.py
- 如果有新模组需要pip安装，记录在./py_script/utils_env_init/pip_requirements.txt，然后在前端的设置页里点击【python环境初始化】按钮。（按钮可能会因为权限问题报错，手动运行./py_script/utils_env_init/setup_venv.py，注意设置安装目录）



## 开发记录

- 参见 ./0-docs/develop.md