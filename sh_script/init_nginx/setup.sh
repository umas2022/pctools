#! /bin/bash


# ### - init_nginx [nginx静态页面服务器]
# - 脚本调用  
# ```./setup.sh```
# - 参数修改
#     - index.html文件位置：init_nginx/frontend.conf - server.root (line 12)
#     - 登录用户名：init_nginx.nginx.conf - user (line 1)
# - 注意
#     - 默认端口8080


# 切换工作目录
cd `dirname $0`

# 参数：端口
port=4080
# 参数：dist文件路径
# dist_path="/root/umasbox/frontend/dist"
dist_path="/mnt/d/s-linux/project/onebox/server_frontend/dist"

# 确认参数
echo -e "\nnginx port: $port"
echo -e "dist path: $dist_path\n\npress enter to continue..."
read -r input

# 创建.user_profile文件并写入.bashrc启动项
if [ ! -e ~/.user_profile ];then
    touch ~/.user_profile
else
    echo "user_profile already exist"
fi
if !( cat ~/.bashrc | grep "user_profile" > /dev/null );then
    echo -e "\necho 'setup command : ~/.user_profile'\n" >> ~/.bashrc
    echo -e "if [ -f ~/.user_profile ]; then\n\t. ~/.user_profile\nfi" >> ~/.bashrc
else
    echo "user_profile already loaded in bashrc"
fi

# 参数写入conf
if cat './frontend.conf' | grep "listen" > /dev/null ;then
    sed -i "/listen*/c\ \tlisten $port;" ./frontend.conf
fi
if cat './frontend.conf' | grep "root" > /dev/null ;then
    sed -i "/root*/c\ \troot $dist_path;" ./frontend.conf
fi

apt update
apt install nginx -y

cp frontend.conf /etc/nginx/conf.d/frontend.conf
cp nginx.conf /etc/nginx/nginx.conf

if !( cat '~/.user_profile' | grep "^service nginx start" > /dev/null );then
    echo "# user profile: nginx" >> ~/.user_profile
    echo "echo ' * nginx port $port starting ...'" >> ~/.user_profile
    echo "service nginx start" >> ~/.user_profile
fi

service nginx stop
nginx -c /etc/nginx/nginx.conf
nginx -s reload

echo -e "\nnginx setup finish\n"
