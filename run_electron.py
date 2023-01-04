'''
2023.1.4
启动electron开发模式
首先将python脚本拷贝到electron的静态目录下
'''

import os
import codecs
import markdown  # pip install markdown
from shutil import copytree, rmtree, copyfile

print("copy backend_v2 file ...")

# 拷贝python文件
if os.path.exists("./desktop_v2/public/static/backend_v2"):
    rmtree("./desktop_v2/public/static/backend_v2")
copytree("./backend_v2", "./desktop_v2/public/static/backend_v2")

# 开发日志转化为html
if os.path.isfile("./desktop_v2/public/static/info/develop.html"):
    os.remove("./desktop_v2/public/static/info/develop.html")
input_file = codecs.open("./0-docs/develop.md", mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text)
output_file = codecs.open("./desktop_v2/public/static/info/develop.html", mode="w", encoding="utf-8")
output_file.write(html)


# 启动electron
os.chdir("./desktop_v2")
os.system("npm run electron:serve")
