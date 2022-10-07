'''
create: 2022.10.5
bookwalker漫画《夜夜夜》爬虫
思路:去除自动化功能,手动启动页面后转交selenium,代码仅执行截图

chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\\p-data\\chrome_temp"

https://bookwalker.jp/de57a21d74-d918-47df-b22f-b3a9454e59df/

问题：截图清晰度很低
'''

import time
import threading
import os
import sys
sys.path.append("..")
from utils_logger.log import logger_re as logger

from selenium import webdriver  # pip install selenium
# 查找元素
from selenium.webdriver.common.by import By
# 添加反爬参数
from selenium.webdriver import ChromeOptions
# 键盘输入
from selenium.webdriver.common.keys import Keys
# 鼠标动作
from selenium.webdriver.common.action_chains import ActionChains

wait_here = input("start ...")

'''实例化浏览器'''
option = ChromeOptions()
option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
# 实例化谷歌
chrome_driver = r"D:\p-tools\chromedriver\chromedriver106.exe"
driver = webdriver.Chrome(executable_path=chrome_driver, options=option)
# 窗口尺寸不能超过显示尺寸,只能考虑找一台高分辨率显示器
# driver.set_window_size(1080,1920)

'''进入漫画页并逐页截屏'''
# 当前激活标签页为0
driver.switch_to.window(driver.window_handles[0])
total = 226
for i in range(total):
    # 等待loading状态结束
    div_loading = driver.find_element(By.CSS_SELECTOR, 'div[class="loading"')
    while div_loading.is_displayed():
        print("waiting")
        time.sleep(1)
    # 浏览器全屏截图(没有找到合适的图片容器)
    time.sleep(1)
    print("shot : %d / %d" % (i, total))
    driver.save_screenshot("./save/shot_%d.png" % i)
    ActionChains(driver).move_by_offset(100, 450).click().move_by_offset(-100, -450).perform()
    # wait_here = input("next : %d " % (i + 1))

wait_here = input("exit ...")
driver.quit()
