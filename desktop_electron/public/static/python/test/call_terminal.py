# 目前存在问题，弹窗不能持续存在

import subprocess
print("start from call_terminal.py")
subprocess.run(['python3', './hello_world.py', "parameter_1"], creationflags=subprocess.CREATE_NEW_CONSOLE)
wait_exit = input("press enter to exit ...\n")
