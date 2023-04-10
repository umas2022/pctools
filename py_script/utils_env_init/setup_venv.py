'''
2023.4.10
创建虚拟环境并在虚拟环境中运行setup.py
'''

import subprocess
import sys
import os

# 脚本位置
setup_dir = os.path.split(os.path.realpath(__file__))[0]
script = os.path.join(setup_dir, "setup.py")

# 项目位置
pctools_path = os.path.dirname(os.path.dirname(setup_dir))
venv_path = os.path.normpath(os.path.join(pctools_path, "venv"))

# 虚拟环境位置
vpython = os.path.normpath(os.path.join(pctools_path, "venv\\Scripts\\python.exe"))
vpip = os.path.normpath(os.path.join(pctools_path, "venv\\Scripts\\pip.exe"))

subprocess.run("pip install virtualenv", creationflags=subprocess.CREATE_NEW_CONSOLE)
subprocess.run("virtualenv -p python3.9 %s" % venv_path, creationflags=subprocess.CREATE_NEW_CONSOLE)
subprocess.run([vpython, script,vpip], creationflags=subprocess.CREATE_NEW_CONSOLE)
