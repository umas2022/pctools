import sys
import os
dic_upper = os.path.abspath(os.path.join(os.getcwd(), "..")) # 上级目录 /root/onebox
dic_add = os.path.join(dic_upper, "py_script") # toolbox目录 /root/onebox/py_script
sys.path.append(dic_upper)
sys.path.append(dic_add)

from py_script.box_copy_batch.terminal import Terminal

import time

path_in = sys.argv[1]
path_out = sys.argv[2]
target = sys.argv[3]
method = sys.argv[4]
ter = Terminal(path_in=path_in,path_out=path_out,target=target,method=method)
ter.start_auto()
wait = input("process finish, press enter to exit ...")

