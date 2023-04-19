'''
2023.1.4
打包electron项目
'''

import os
import sys
import codecs
from shutil import copytree, rmtree, copyfile
import markdown  # pip install markdown
import json
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

# config.json重设初值
print("init default config ...")
config_json = {}
with open("./desktop_electron/public/static/config.json", "r", encoding="utf-8")as config_file:
    config_json = json.load(config_file)
    config_json["py_path"]["value"] = ""
    config_json["py_server"]["value"] = ""
with open("./desktop_electron/public/static/config.json", "w", encoding="utf-8") as config_file:
    config_file.write(json.dumps(config_json, ensure_ascii=False) + "\n")

# 开发日志转化为html
print("develop.md format convert ...")
if os.path.isfile("./desktop_electron/public/static/info/develop.html"):
    os.remove("./desktop_electron/public/static/info/develop.html")
input_file = codecs.open("./0-docs/develop.md", mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text)
output_file = codecs.open("./desktop_electron/public/static/info/develop.html", mode="w", encoding="utf-8")
output_file.write(html)

# 执行打包命令
subprocess.run(["npm", "run", "electron:build"], cwd="./desktop_electron", stdout=subprocess.PIPE,shell=True)

# # 删除python文件
print("remove server & script ...")
rmtree("./desktop_electron/public/static/py_server")
rmtree("./desktop_electron/public/static/py_script")
