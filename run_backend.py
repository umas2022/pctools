'''
2023.1.4
调试时快捷启动后端
'''

import subprocess
import sys,os


setup_dir = os.path.split(os.path.realpath(__file__))[0]

script = os.path.join(setup_dir,"backend_v2/run_backend.py")
print("backend: %s" %script)
print("running ...")

if len(sys.argv) == 1:
    # 无参数直接默认启动
    subprocess.run(['python', script], creationflags=subprocess.CREATE_NEW_CONSOLE)
else:
    # 有参数把参数传给run_backend.py
    subprocess.run(['python', script, sys.argv[1]], creationflags=subprocess.CREATE_NEW_CONSOLE)

print("backend server close")
