'''
2023.1.4
启动electron开发模式
首先将python脚本拷贝到electron的静态目录下
'''

import os

from shutil import copytree,rmtree
print("copy backend_v2 file ...")
if os.path.exists("./desktop_v2/public/static/backend_v2"):
    rmtree("./desktop_v2/public/static/backend_v2")
copytree("./backend_v2","./desktop_v2/public/static/backend_v2")

os.chdir("./desktop_v2")
os.system("npm run electron:serve")


