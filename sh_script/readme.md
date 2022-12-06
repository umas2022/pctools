# init环境初始化配置脚本readme


## 脚本编写规范
- 调用脚本统一命名为文件夹下setup.sh
- 脚本如有使用同级目录下文件，使用cd `dirname $0`切换工作目录，保证在shellbox级可以直接调用
- 启动命令统一存放在~/.user_profile，不再对.bashrc进行操作
- 若脚本有可变参数，需输出当前值并要求回车确认
  
  





















