'''
create: 2022.12.4
bookwalker漫画《妖精森林的小不点》爬虫
思路:去除自动化功能,手动启动chrome打开debug端口,转交selenium,代码仅执行截图,两块显示器上下拼接扩大网页显示范围,结束后执行图片低度锐化
问题:截图清晰度受屏幕分辨率影响,质量较低

chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\\p-data\\chrome_temp"

https://bookwalker.jp/bookshelf1/

'''


# 总页数
total_page = 5
# 图片保存位置(路径下不要有其他图片)
save_path = r"D:\s-workspace\crawler_save"
# 图片锐化系数(1为原图,实测2效果还行)
sharp_factor = 2

import time
import threading
import os
import sys
# 图片锐化
from PIL import Image, ImageEnhance
# 爬虫主程序
from selenium import webdriver  # pip install selenium
# 查找元素
from selenium.webdriver.common.by import By
# 添加反爬参数
from selenium.webdriver import ChromeOptions
# 键盘输入
from selenium.webdriver.common.keys import Keys
# 鼠标动作
from selenium.webdriver.common.action_chains import ActionChains

wait_here = input("press enter to start ...")

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
for i in range(total_page):
    # 等待loading状态结束
    div_loading = driver.find_element(By.CSS_SELECTOR, 'div[class="loading"')
    while div_loading.is_displayed():
        print("waiting")
        time.sleep(1)
    # 浏览器全屏截图
    time.sleep(1)
    print("shot : %d / %d" % (i + 1, total_page))
    driver.save_screenshot(os.path.join(save_path, "shot_%d.png" % i+1))
    ActionChains(driver).move_by_offset(100, 450).click().move_by_offset(-100, -450).perform()
    # wait_here = input("next : %d " % (i + 1))

wait_here = input("shot-function finish \npress enter to start sharpen-function ...")
driver.quit()


'''图片锐化'''
def get_file(path_in):
    for root, dirs, files in os.walk(path_in):
        for fileName in files:
            full_path = os.path.join(root, fileName).replace('\\', "/")
            yield full_path
i = 0
for shot_path in get_file(save_path):
    i += 1
    print("sharpen : %d / %d" % (i, total_page))
    img = Image.open(shot_path)
    enhancer = ImageEnhance.Sharpness(img)
    im_s = enhancer.enhance(sharp_factor)
    sharp_path = shot_path.split(".")
    sharp_path[-2] += "_sharp"
    sharp_path = ".".join(sharp_path)
    im_s.save(sharp_path)
    os.remove(shot_path)

wait_here = input("sharpen-function finish \npress enter to exit ...")
