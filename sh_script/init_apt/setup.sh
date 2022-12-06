#! /bin/bash

# ### - init_apt [apt软件包安装]
# - 脚本调用  
# ```./setup.sh```  
# - 参数修改  
#     - 添加新的包：/init_apt/apt_requirements.txt

# 切换工作目录
cd `dirname $0`

# apt 软件包安装
echo -e "\n ========== update ========== \n"
apt update
cat 'apt_requirements.txt' | while read line
do
    if [[ $line != "" ]];then 
        if [[ $line != *"#"* ]];then
            echo -e "\n ========== install $line ========== \n"
            apt install $line -y
        fi
    fi
done
