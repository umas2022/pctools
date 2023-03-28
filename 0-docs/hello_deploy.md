# 项目部署记录

# 此文档已经(懒得更新了)

# 戴尔G3
- **项目文件路径：D:\s-linux\project\onebox**

- 打开windows启动项文件夹：win+R, shell:startup
- windows启动脚本：C:\Users\umas\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\startup.vbs

- **工具箱前端nginx在wls启动, 端口[4080]**
    - wsl中nginx端启动命令写在bashrc中：/root/.user_profile
    - 在windows中调出wsl即可自动运行, vbs启动脚本如下：
    ```vb
    ' start nginx frontend, port 4080
    Set ws=WScript.CreateObject("WScript.Shell") 
    ' ws.Run "wsl -d Ubuntu-20.04 -u root /bin/bash",0
    ws.Run "wsl -u root /bin/bash",0
    ```

- **工具箱后端在powershell中启动, 端口[4090]**
    - vbs启动脚本：
    ```vb
    ' start django backend, port 4090
    Set ws=WScript.CreateObject("WScript.Shell") 
    ws.Run "python.exe D:\s-linux\project\onebox\run_backend.py",0
    ```

- **code-server在wsl中启动, 端口[8081]**
    - 位置在/root/.user_profile


- **wsl默认启动ssh, 端口[64822]**
    - 位置在/root/.user_profile
