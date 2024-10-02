'''
create: 2022.10.5
bookwalker漫画《夜夜夜》爬虫
思路:命令行启动浏览器,用selenium接管,不用考虑登录问题,也不需要反爬(浏览器要有登录信息)
bookwalker的图片是以canvas形式展示的,没办法直接拿到原图,只能考虑截图了
多次登录仍然会触发谷歌人机认证,推荐的方法是用命令行启动一个常开的浏览器,避免多次登录
chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\\p-data\\chrome_temp"

问题:由于无法判断图片是否加载完毕,完全的自动化很难实现,考虑采用手动
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

url_top = "https://bookwalker.jp/top/"
url_login = "https://member.bookwalker.jp/app/03/login"
url_home = "https://bookwalker.jp/de57a21d74-d918-47df-b22f-b3a9454e59df/"
url_manga = "https://viewer.bookwalker.jp/03/20/viewer.html?cid=57a21d74-d918-47df-b22f-b3a9454e59df&cty=1"

'''实例化浏览器'''
# 反爬：接管已打开的浏览器


def run_chrome():
    os.system('chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\\p-data\\chrome_temp"')


th_chrome = threading.Thread(target=run_chrome)
# th_chrome.start()
time.sleep(1)
option = ChromeOptions()
option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
# 实例化谷歌
chrome_driver = r"D:\p-tools\chromedriver\chromedriver106.exe"
driver = webdriver.Chrome(executable_path=chrome_driver, options=option)


'''进入home页打开漫画'''
driver.get(url=url_home)
driver.implicitly_wait(30)
driver.find_element(By.CSS_SELECTOR, 'a[class="a-basic-btn--read a-basic-btn"').click()

'''首次进入需要确认登录'''
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(30)
if driver.current_url == "https://member.bookwalker.jp/app/03/login":
    driver.find_element(By.CSS_SELECTOR, 'button[id="recaptchaLoginBtn"').click()

'''进入漫画页并逐页截屏'''
wait_here = input("start ...")
for i in range(250):
    driver.implicitly_wait(30)
    div = driver.find_element(By.CSS_SELECTOR, 'div[id="root"')
    # 这里缺少一个方法判断图片是否已经加载出来了
    div.screenshot("./save/shot_%d.png" % i)
    wait_here = input("next : %d" % (i + 1))
    ActionChains(driver).move_by_offset(100, 300).click().perform()

wait_here = input("exit ...")
driver.quit()
