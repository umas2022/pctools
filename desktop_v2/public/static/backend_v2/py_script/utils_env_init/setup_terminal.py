'''
2023.1.29
给setup.py单独起一个终端
'''

import subprocess
import sys,os


setup_dir = os.path.split(os.path.realpath(__file__))[0]

script = os.path.join(setup_dir,"setup.py")

subprocess.run(['python', script], creationflags=subprocess.CREATE_NEW_CONSOLE)
