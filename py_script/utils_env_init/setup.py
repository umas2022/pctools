'''
2022.1.4
初始化安装运行库
1. 直接使用pip -r requirements.txt在windows环境下会出现gbk编码错误,改为手动读取txt每一行
2. 支持一个输入参数pip,可以指定使用的pip(比如虚拟环境pip),无输入时使用默认pip
'''
import os
import sys


pip_cmd = "pip"
if len(sys.argv) > 1:
    pip_cmd = sys.argv[1]

use_tsinghua = False
th_source = "https://pypi.tuna.tsinghua.edu.cn/simple"
print("\npip command : %s (pip/pip3)" % pip_cmd)
print("use tsinghua source : %s\n" % str(use_tsinghua))


setup_dir = os.path.split(os.path.realpath(__file__))[0]
requirements_txt = os.path.join(setup_dir, "pip_requirements.txt")

with open(requirements_txt, "r", encoding="utf-8") as re_file:
    for module in re_file.readlines():
        module = module.strip()
        if not (module == "" or "#" in module):
            if use_tsinghua:
                os.system("%s install -i  %s %s" % (pip_cmd, th_source, module))
            else:
                os.system("%s install %s" % (pip_cmd,module))

wait_here = input("\n\npress enter to exit ...")
