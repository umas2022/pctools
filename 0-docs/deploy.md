# 项目部署


### 后端python环境

1. 使用虚拟环境（推荐）（开发时所用python版本为3.10）
```
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate
```
2. 安装python依赖
```
python.exe .\py_script\utils_env_init\setup.py
```
3. 验证安装，启动后端
```
python.exe run_backend.py
初次运行可能会提示需要 python manage.py migrate
```

### 前端node环境
1. 下载安装[node.js](https://nodejs.org/en)，注意项目所用node版本为16.15.1；安装时记得勾选 Automatically xxx 
2. 不同版本node使用nvm控制，[GitHub下载](https://github.com/coreybutler/nvm-windows/releases/tag/1.1.11)
3. 安装node模组
```
cd .\desktop_electron\
npm i
```
  - 新电脑安装模组时可能会报 looking for Visual Studio 2015 - not found 之类的错误，可以跑一下3dm游戏运行库  

3. 验证安装，启动前端
```
python.exe .\run_electron.py
或（前端目录下）: npm run electron:serve
```
  - 报错：Error: Electron failed to install correctly, please delete node_modules/electron and try installing again；应该是因为网络问题electron没有安装成功，删除后使用cnpm重新安装（注意版本）：
```
npm i cnpm -g
cnpm install electron@13
```
 - 报错：Error: error:0308010C:digital envelope routines::unsupported ...；发现node版本太高会报错，使用nvm控制node版本16.15.1，注意改变node版本之后node_modules要删除重新下载


 ### Run
- dev: run backend server  
```python run_backend.py```
- dev: run electron server (develop mode)
```python run_electron.py```

## Build
- dev: build electron package
```python build_electron.py```