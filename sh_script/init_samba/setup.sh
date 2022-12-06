#! /bin/bash

# ### - init_samba [samba局域网文件共享]
# - 脚本调用  
# ```./setup.sh```
# - 参数修改
#     - 系统适配(ubuntu/raspbian)：/init_samba/setup.sh - 选择conf文件(line9)
#     - 共享文件夹参数：/init_samba/smb.conf - [public] (line243)


# 切换工作目录
cd `dirname $0`


package="samba"
if  type $package > /dev/null 2>&1;then
    echo "$package already installed"
else
    apt update
    apt install $package -y
fi


cp /etc/samba/smb.conf /etc/samba/smb.conf.bk
# cp smb_ubuntu.conf /etc/samba/smb.conf
cp smb_raspbian.conf /etc/samba/smb.conf
printf "umas1970\numas1970" | smbpasswd -a root
samba restart
