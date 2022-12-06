#! /bin/bash

# ### - rpi_source [树莓派改国内源]
# - 脚本调用  
# ```./setup.sh```
# - 参数修改
#     - 源修改：同级list文件

# # 软件源更新报错
# cp /etc/apt/sources.list /etc/apt/sources.list.bk
# cp sources.list  /etc/apt/sources.list 

# # 系统更新源报错
# cp /etc/apt/sources.list.d/raspi.list /etc/apt/sources.list.d/raspi.list.bk
# cp raspi.list /etc/apt/sources.list.d/raspi.list 

apt update

