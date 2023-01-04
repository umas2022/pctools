'''
2023.1.4
电脑配件后端初始化脚本
'''

import os
import json
import subprocess

setup_dir = os.path.split(os.path.realpath(__file__))[0]


print("\n\n ========== 初始化配置文件(1) ========== \n\n")
config_json = json.load(open("./user_config.json", "r", encoding="utf-8"))
config_json["frontend"]["py_path"] = setup_dir
with open("./user_config.json", "w", encoding="utf-8") as config_file:
    config_file.write(json.dumps(config_json, ensure_ascii=False) + "\n")
print("\nconfig.json init : done ...\n")


print("\n\n ========== 安装script运行库(2) ========== \n\n")
script_setup = os.path.join(setup_dir, "py_script/utils_env_init/setup.py")
subprocess.run(["python", script_setup])
print("\nscript env init : done ...\n")

print("\n\n ========== 安装server运行库(3) ========== \n\n")
script_setup = os.path.join(setup_dir, "py_server/server_env_init/setup.py")
subprocess.run(["python", script_setup])
print("\nscript env init : done ...\n")
