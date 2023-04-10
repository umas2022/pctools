'''
2023.1.4
包内部启动后端,被run_backendterminal.py终端脚本调用
'''
import os
import sys
import argparse

# 两个输入参数:端口和python版本
parser = argparse.ArgumentParser(description='Script description')
parser.add_argument('-p', '--port', type=str, required=False, help='Port number')
parser.add_argument('-v', '--version', type=str, required=False, help='Version number')
args = parser.parse_args()

# 脚本所在路径
server_path = os.path.split(os.path.realpath(__file__))[0]
os.chdir(server_path)

py_version = args.version if args.version else "python"
port = args.port if args.port else 4090

print("python version in use: %s" % py_version)
print("backend port: %s\n" % port)
print("server path: %s" % server_path)


os.system("%s manage.py runserver 0.0.0.0:%s" % (py_version, port))



