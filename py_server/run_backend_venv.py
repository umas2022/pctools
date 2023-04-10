
'''
2023.4.10
在虚拟环境中启动后端
electron手动启动后端时调用此脚本
'''

import subprocess
import sys
import os

# 脚本位置
server_path = os.path.split(os.path.realpath(__file__))[0]
script = os.path.join(server_path, "run_backend.py")
print("backend: %s" % script)
print("running ...")

# 项目位置
pctools_path = os.path.dirname(server_path)
venv_path = os.path.normpath(os.path.join(pctools_path, "venv"))

# 虚拟环境位置
vpython = os.path.normpath(os.path.join(pctools_path, "venv\\Scripts\\python.exe"))
vpip = os.path.normpath(os.path.join(pctools_path, "venv\\Scripts\\pip.exe"))


if len(sys.argv) == 1:
    # 无参数直接默认启动
    subprocess.run([vpython, script, "-v", vpython], creationflags=subprocess.CREATE_NEW_CONSOLE)
else:
    # 支持一个输入参数port,直接传给run_backend.py
    subprocess.run([vpython, script, "-v", vpython, "-p", sys.argv[1]], creationflags=subprocess.CREATE_NEW_CONSOLE)

print("backend server close")
