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
print("copy backend_v2 file ...")
if os.path.exists("./desktop_electron/public/static/backend_v2"):
    rmtree("./desktop_electron/public/static/backend_v2")
copytree("./backend_v2", "./desktop_electron/public/static/backend_v2")

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
