'''
create: 2022.10.5
bookwalker漫画《夜夜夜》爬虫
思路:去除自动化功能,手动启动页面后转交selenium,代码仅执行截图

chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\\p-data\\chrome_temp"

https://bookwalker.jp/de57a21d74-d918-47df-b22f-b3a9454e59df/

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


'''实例化浏览器'''
wait_here = input("take over the browser ...")
option = ChromeOptions()
option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
# 实例化谷歌
chrome_driver = r"D:\p-tools\chromedriver\chromedriver106.exe"
driver = webdriver.Chrome(executable_path=chrome_driver, options=option)


'''进入漫画页并逐页截屏'''
wait_here = input("start ...")
# 当前激活标签页为0
driver.switch_to.window(driver.window_handles[0])
i = 0
# ActionChains(driver).move_by_offset(100, 450).perform()

while True:
    i += 1
    # div = driver.find_element(By.CSS_SELECTOR, 'div[id="root"')
    driver.save_screenshot("./save/shot_%d.png" % i)
    ActionChains(driver).move_by_offset(100, 450).click().move_by_offset(-100, -450).perform()
    # time.sleep(2)
    wait_here = input("next : %d (enter:next; e:exit)" % (i + 1))
    if wait_here == "e":
        break

wait_here = input("exit ...")
driver.quit()
