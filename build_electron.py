'''
2023.1.4
打包electron项目
'''

import os
import codecs
from shutil import copytree, rmtree, copyfile
import markdown  # pip install markdown

# 虽然在vue.config.js中已经设置了包含python文件夹,但并不能自动更新,仅在public下不存在python文件夹时才能打包进去
# 所以仍然需要手动拷贝更新python文件夹 

# 拷贝python文件
print("copy python file ...")
if os.path.exists("./desktop_electron/public/static/py_script"):
    rmtree("./desktop_electron/public/static/py_script")
copytree("./py_script", "./desktop_electron/public/static/py_script")
if os.path.exists("./desktop_electron/public/static/py_server"):
    rmtree("./desktop_electron/public/static/py_server")
copytree("./py_server", "./desktop_electron/public/static/py_server")

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
os.chdir("./desktop_electron")
os.system("npm run electron:build")

# 删除python文件 # 直接在这里删除的话打包命令还没运行完
# rmtree("./desktop_electron/public/static/py_server")
# rmtree("./desktop_electron/public/static/py_script")


