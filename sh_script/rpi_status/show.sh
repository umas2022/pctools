#! /bin/bash

# ### - rpi_status.sh [显示树莓派状态：温度]
# - 脚本调用  
# ```./show.sh```


while [ true ]; do

    # 输出时间
    date

    # cpu温度
    get_temp=`cat /sys/class/thermal/thermal_zone0/temp`
    temprature=`echo "scale=3; $get_temp/1000" | bc`
    echo "temperature: $temprature C"

    # 网络监控
    cat /proc/net/dev

    # cpu占用
    

    # 内存占用


    # 睡眠1秒，清屏
    /bin/sleep 1
    clear
done




