import os
import sys

# # 激活虚拟环境
# print("\nactivate virtualenv by: source env/bin/activate\n")

win_path = r"D:\s-linux\project\pctools\backend_v2\py_server"
wsl_path = r"/mnt/d/s-linux/project/pctools/py_server"
py_version = "python"
# py_version = "python3"
print("python version in use: %s" % py_version)
print("default win path: %s\ndefault wsl path: %s\n" % (win_path, wsl_path))

# 无输入参数时认为是在box目录下直接调用的
if len(sys.argv) == 1:
    print("\n\tbackend use default port:4090\n")
    os.chdir("./py_server")
    os.system("%s manage.py runserver 0.0.0.0:4090" % py_version)

# 输入"win"调用完整windows目录
elif sys.argv[1] == "win":
    os.chdir(win_path)
    os.system("%s manage.py runserver 0.0.0.0:4090" % py_version)

# 输入"wsl"调用完整wsl目录
elif sys.argv[1] == "wsl":
    os.chdir(wsl_path)
    os.system("%s manage.py runserver 0.0.0.0:4090" % py_version)

# 也可以直接输入端口号, 开发模式使用端口4091
else:
    port = sys.argv[1]
    print("\n\tbackend port: %s\n" % port)
    os.chdir("./py_server")
    print("%s manage.py runserver 0.0.0.0:%s" % (py_version, port))
    os.system("%s manage.py runserver 0.0.0.0:%s" % (py_version, port))



