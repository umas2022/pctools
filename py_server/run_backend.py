'''
2023.1.4
包内部启动后端,被run_backendterminal.py终端脚本调用

脚本测试

python run_backend.py -p 4090 -v D:\p-program\pctools_venv\venv\Scripts\python.exe
D:\p-program\pctools_venv\venv\Scripts\python.exe run_backend.py -p 4090 -v python
'''
import os
import sys
import argparse

# 两个输入参数:端口和python版本
parser = argparse.ArgumentParser(description='Script description')
parser.add_argument('-p', '--port', type=str, required=False, help='Port number')
parser.add_argument('-v', '--version', type=str, required=False, help='Python version')
args = parser.parse_args()

# 脚本所在路径
server_path = os.path.split(os.path.realpath(__file__))[0]
os.chdir(server_path)

py_version = args.version if args.version else "python"
port = args.port if args.port else 4090

print("python in use: %s" % py_version)
print("backend port: %s" % port)
print("server path: %s\n" % server_path)


os.system("%s manage.py runserver 0.0.0.0:%s" % (py_version, port))



