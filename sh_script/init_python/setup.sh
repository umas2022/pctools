#! /bin/bash

# ### - init_python [python环境初始化]
# - 脚本调用  
# ```python3 setup_tsinghua.py```   
# ```python3 setup.py```  
# ```./setup.sh```
# - 参数修改
#     - 添加新的包：/init_python/pip_requirements.txt
# - 注意 
#     - py文件适用于window平台
# 	- termux环境下清华源可能报错，使用原生setup.py
#     - 若仍然出现报错可以尝试更新pip  


# 切换工作目录
cd `dirname $0`

pip3 install -r pip_requirements.txt
