# 未来可能实现的功能（想起来但懒得做的功能）和一些问题不大的bug

### frontend
- new: 增加help页面, 最好附上图片, 处理前->处理后
- new: 网页显示文件目录, ftp之类的, 网页samba
- new: 前端统计显示error和warning信息
- new: 进度条
- new: 增加linux环境shell工具的支持
- new：进程开始之后没法手动停止, 大批量处理时还是很卡, 处理完成了没也不知道
- new：各输入框记住上次的输入,搞一个json存起来

- 重命名：前端重命名功能支持[动作叠加], 如先删括号再加前缀
- 重命名：copy_to_one增加选项：命名是否合并上一级文件夹名

- 重命名/复制：copy和backup的统计信息单独显示一个框, 总大小, 数量之类
- 重命名/复制：python工具清空按钮应该把所有选项都重置, 而不是只有路径
- 重命名/复制：目标不仅限于文件/文件夹, 可以按后缀名分类


### backend
- new: 首页增加项目一键部署到远程主机功能
- new: 返回当前环境 uname -a 或者是自定义的设备标识, wsl/dell/raspi
- 后端允许了所有跨域请求, 不安全

### py_script
- py_script：增加更多接口给前端, 比如img_cut自定义压缩上限, 是否反向删除
- box_backup：rename的命令行输出文件总数是0
- box_backup：rename.by_number把子文件夹里的文件也顺序编号了
- box_backup：反向对比删除空文件夹
- box_backup：备份时间txt不能写入, 每次都是新的
- box_rename_batch：有输出路径时先拷贝再命名这个逻辑不对, 如果输出目录中已经存在一些文件, 会一起被重命名, 对文件夹操作时若已存在和重命名结果同名的文件夹, makedir函数会报错已存在同名文件夹
- box_copy_batch: 图片压缩对bmp失败


### tools_shell
- 不搞linux了,这部分不更了


### others
- 推荐使用虚拟环境（目前powershell报错, 暂时搁置）
    ```
    pip3 install virtualenv -i  https://pypi.tuna.tsinghua.edu.cn/simple
    virtualenv -p python3.8 env 
    source env/bin/activate
    deactivate 
    ```


### 已解决/不想解决
- new: 换个图标
- 前端home获取ip偶尔还是会被跨域block
- 主页：网页远程命令行功能太简单, 目前还不能接受报错, 不能cd切换目录, 也没有当前目录提示
- py_script：文件夹目录中间修改了一次, import可能报错, 还没改完
- rename: 删除括号扩展为删除任意前缀




