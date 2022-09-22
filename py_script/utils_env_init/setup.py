import os

pip_cmd = "pip"
use_tsinghua = False
th_source = "https://pypi.tuna.tsinghua.edu.cn/simple"
print("\npip command : %s (pip/pip3)" % pip_cmd)
print("use tsinghua source : %s" % str(use_tsinghua))
confirm = input("\npress enter to continue ...")

if use_tsinghua:
    os.system("%s install -i  %s -r pip_requirements.txt" %
              (pip_cmd, th_source))
else:
    os.system("%s install -r pip_requirements.txt" % pip_cmd)
