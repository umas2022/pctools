'''
2023.1.4
启动electron开发模式
首先将python脚本拷贝到electron的静态目录下
'''

import os
import sys
import codecs
import markdown  # pip install markdown
from shutil import copytree, rmtree, copyfile
import subprocess

# 更新script目录
print("update list.json ...")
prj_path = os.path.dirname(os.path.realpath(__file__))
script_path = os.path.normpath(os.path.join(prj_path, "py_script"))
sys.path.append(prj_path)
from py_script.utils_update_list.update import list_update
list_update(script_path)

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


# # 启动electron
subprocess.run(["npm", "run", "electron:serve"], cwd="./desktop_electron", stdout=subprocess.PIPE,shell=True)


# # 删除python文件
print("remove server & script ...")
rmtree("./desktop_electron/public/static/py_server")
rmtree("./desktop_electron/public/static/py_script")
