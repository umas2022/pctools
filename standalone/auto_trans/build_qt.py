'''
qt项目打包脚本
除基本打包命令外删除了临时文件
'''

import os
from shutil import rmtree
from shutil import copytree, copyfile

op_name = "独立电脑配件-自助翻译"


# 执行打包命令 -w 参数终端不显示

os.system("pyinstaller.exe -F -n %s \
           --add-data component;component \
           --add-data D:\\s-code\\self\pctools\\venv\\Lib\\site-packages\\pykakasi\\data;pykakasi/data \
            .\\app.py" % op_name)



# 删除多余文件
os.remove("%s.spec" % op_name)
rmtree("./build")
