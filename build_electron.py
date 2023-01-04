'''
2023.1.4
打包electron项目
'''

import os

## 打包时这里不再拷贝python文件夹,在vue.config.js中已经设置了包含python文件夹

# from shutil import copytree,rmtree
# print("copy backend_v2 file ...")
# if os.path.exists("./desktop_v2/public/static/backend_v2"):
#     rmtree("./desktop_v2/public/static/backend_v2")
# copytree("./backend_v2","./desktop_v2/public/static/backend_v2")

os.chdir("./desktop_v2")
os.system("npm run electron:build")


