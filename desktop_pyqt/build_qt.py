'''
qt项目打包脚本
除基本打包命令外删除了临时文件
'''

import os
from shutil import  rmtree

# op_name = "电脑配件qt"
op_name = "window"


os.system("pyinstaller.exe -F -w -n %s \
           -i .\\resource\\img\\mati_ei_256.ico \
           --add-data resource;resource \
            .\\window.py" % op_name)

os.remove("%s.spec" % op_name)
rmtree("./build")
