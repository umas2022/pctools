# 为后端开启新的终端
# electron手动启动后端时调用此脚本

import subprocess
import sys

script = r"D:\s-linux\project\pctools\backend_v2\run_backend.py"
print("backend: %s" %script)
print("running ...")

if len(sys.argv) == 1:
    subprocess.run(['python3', script], creationflags=subprocess.CREATE_NEW_CONSOLE)
else:
    subprocess.run(['python3', script, sys.argv[1]], creationflags=subprocess.CREATE_NEW_CONSOLE)

print("backend server close")
