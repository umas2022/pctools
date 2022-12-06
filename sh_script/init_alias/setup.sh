#! /bin/bash

user="root"


# 确认参数
echo -e "\nuser: $user\npress enter to continue..."
read -r input


# 创建.user_profile文件并写入.bashrc启动项
if [ ! -e /$user/.user_profile ];then
    touch /$user/.user_profile
else
    echo "user_profile already exist"
fi
if !( cat /$user/.bashrc | grep "user_profile" > /dev/null );then
    echo -e "\necho 'setup command : /$user/.user_profile'\n" >> /$user/.bashrc
    echo -e "if [ -f /$user/.user_profile ]; then\n\t. /$user/.user_profile\nfi" >> /$user/.bashrc
else
    echo "user_profile already loaded in bashrc"
fi

cmd_arr=("alias cdbox='cd /mnt/d/s-linux/project/onebox'" \
        "alias boxback='python3 run_backend.py'" \
        "")

for cmd in "${cmd_arr[@]}";do
    echo $cmd
    if !( cat /$user/.user_profile | grep "$cmd" > /dev/null );then
        echo "# alias" >> /$user/.user_profile
        echo "$cmd" >> /$user/.user_profile
    fi
done

source /$user/.bashrc

echo -e "\nall done\n"
