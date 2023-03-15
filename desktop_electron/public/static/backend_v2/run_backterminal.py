
'''
2023.1.4
为后端开启新的终端
electron手动启动后端时调用此脚本
'''

import subprocess
import sys,os


setup_dir = os.path.split(os.path.realpath(__file__))[0]

script = os.path.join(setup_dir,"run_backend.py")
print("backend: %s" %script)
print("running ...")

if len(sys.argv) == 1:
    # 无参数直接默认启动
    subprocess.run(['python', script], creationflags=subprocess.CREATE_NEW_CONSOLE)
else:
    # 有参数把参数传给run_backend.py
    subprocess.run(['python', script, sys.argv[1]], creationflags=subprocess.CREATE_NEW_CONSOLE)

print("backend server close")
