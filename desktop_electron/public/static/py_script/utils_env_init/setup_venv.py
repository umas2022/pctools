'''
2023.4.10
创建虚拟环境并在虚拟环境中运行setup.py
接收一个参数:虚拟环境位置
'''

import subprocess
import sys
import os

# 前端输入虚拟环境位置
input_path = sys.argv[1]
# 项目位置
setup_dir = os.path.split(os.path.realpath(__file__))[0]
pctools_path = os.path.dirname(os.path.dirname(setup_dir))
# 使用的位置:使用input路径而不是项目路径
user_path = input_path

# setup脚本位置
script = os.path.join(setup_dir, "setup.py")
print("###############")
print(user_path)

# 虚拟环境位置
venv_path = os.path.normpath(os.path.join(user_path, "venv"))
vpython = os.path.normpath(os.path.join(user_path, "venv\\Scripts\\python.exe"))
vpip = os.path.normpath(os.path.join(user_path, "venv\\Scripts\\pip.exe"))

subprocess.run("pip install virtualenv", creationflags=subprocess.CREATE_NEW_CONSOLE)
subprocess.run("virtualenv -p python3.9 %s" % venv_path, creationflags=subprocess.CREATE_NEW_CONSOLE)
subprocess.run([vpython, script, vpip], creationflags=subprocess.CREATE_NEW_CONSOLE)
