'''
2023.1.4
包内部启动后端,被run_backendterminal.py终端脚本调用
'''
import os
import sys

setup_dir = os.path.split(os.path.realpath(__file__))[0]

server_path = os.path.join(setup_dir,"py_server") 
py_version = "python"
# py_version = "python3"
print("python version in use: %s" % py_version)
print("server path: %s" % server_path)

# 无输入参数时认为是在backend_v2目录下直接调用的
if len(sys.argv) == 1:
    print("\n\tbackend use default port:4090\n")
    os.chdir("./backend_v2/py_server")
    os.system("%s manage.py runserver 0.0.0.0:4090" % py_version)

# 输入"win"调用完整windows目录
elif sys.argv[1] == "win":
    os.chdir(server_path)
    os.system("%s manage.py runserver 0.0.0.0:4090" % py_version)

# 也可以直接输入端口号, 开发模式使用端口4091
else:
    port = sys.argv[1]
    print("\n\tbackend port: %s\n" % port)
    os.chdir("./backend_v2/py_server")
    print("%s manage.py runserver 0.0.0.0:%s" % (py_version, port))
    os.system("%s manage.py runserver 0.0.0.0:%s" % (py_version, port))



