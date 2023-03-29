'''
qt项目打包脚本
除基本打包命令外删除了临时文件
'''

import os
from shutil import  rmtree
from shutil import copytree, copyfile

# op_name = "电脑配件qt"
op_name = "window"

# 拷贝python文件
print("copy backend_v2 file ...")
if os.path.exists("./resource/py_script"):
    rmtree("./resource/py_script")
copytree("../backend_v2/py_script", "./resource/py_script")

# 执行打包命令
os.system("pyinstaller.exe -F -w -n %s \
           -i .\\resource\\img\\mati_ei_256.ico \
           --add-data resource;resource \
            .\\window.py" % op_name)

# 删除多余文件
os.remove("%s.spec" % op_name)
rmtree("./build")
