'''
2023.1.4
调试时快捷启动后端
这个脚本仅用于开发阶段调试,真正的后端启动脚本是py_server/run_backend.py
'''

import subprocess
import sys,os


# 脚本所在路径
setup_dir = os.path.split(os.path.realpath(__file__))[0]

script = os.path.normpath(os.path.join(setup_dir,"py_server/run_backend.py")) 
print("backend: %s" %script)
print("running ...")

if len(sys.argv) == 1:
    # 无参数直接默认启动
    # subprocess.run(['python', script], creationflags=subprocess.CREATE_NEW_CONSOLE)
    subprocess.run(['python', script])
else:
    # 有参数把参数传给run_backend.py
    subprocess.run(['python', script, sys.argv[1]], creationflags=subprocess.CREATE_NEW_CONSOLE)

print("backend server close")
