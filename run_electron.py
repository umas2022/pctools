'''
2023.1.4
启动electron开发模式
首先将python脚本拷贝到electron的静态目录下
'''

import os
import codecs
import markdown  # pip install markdown
from shutil import copytree, rmtree, copyfile


# 拷贝python文件
print("copy python file ...")
if os.path.exists("./desktop_electron/public/static/py_script"):
    rmtree("./desktop_electron/public/static/py_script")
copytree("./py_script", "./desktop_electron/public/static/py_script")
if os.path.exists("./desktop_electron/public/static/py_server"):
    rmtree("./desktop_electron/public/static/py_server")
copytree("./py_server", "./desktop_electron/public/static/py_server")


# 开发日志转化为html
print("convert develop.md ...")
if os.path.isfile("./desktop_electron/public/static/info/develop.html"):
    os.remove("./desktop_electron/public/static/info/develop.html")
input_file = codecs.open("./0-docs/develop.md", mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text)
output_file = codecs.open("./desktop_electron/public/static/info/develop.html", mode="w", encoding="utf-8")
output_file.write(html)


# 启动electron
os.chdir("./desktop_electron")
os.system("npm run electron:serve")

# 删除python文件 # 直接在这里删除的话打包命令还没运行完
# rmtree("./desktop_electron/public/static/py_server")
# rmtree("./desktop_electron/public/static/py_script")

