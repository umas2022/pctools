'''
create: 2022.12.4
bookwalker漫画《妖精森林的小不点》爬虫
思路:去除自动化功能,手动启动chrome打开debug端口,转交selenium,代码仅执行截图,两块显示器上下拼接扩大网页显示范围,图片锐化和截图双线程同步进行
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
# debug模式chrome数据位置
chrome_path = r"D:\\p-data\\chrome_temp"
chrome_ready = False

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


def sharpen_main(shot_path):
    '''锐化主函数'''
    shot_path_list = shot_path.split("/")
    img = Image.open(shot_path)
    enhancer = ImageEnhance.Sharpness(img)
    im_s = enhancer.enhance(sharp_factor)
    shot_path_list[-1] = shot_path_list[-1].replace("shot", "sharp")
    sharp_path = "/".join(shot_path_list)
    im_s.save(sharp_path)
    os.remove(shot_path)


'''实例化浏览器'''
if not chrome_ready:    
    os.system('chrome.exe --remote-debugging-port=9222 --user-data-dir="%s"' % chrome_path)
    wait_here = input("make sure chrome is ready and press enter to continue ...")
option = ChromeOptions()
option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
# 实例化谷歌
chrome_driver = r"D:\p-tools\chromedriver\chromedriver106.exe"
driver = webdriver.Chrome(executable_path=chrome_driver, options=option)
# 窗口尺寸不能超过显示尺寸,只能考虑找一台高分辨率显示器或者多屏拼接
# driver.set_window_size(1080,1920)

'''进入漫画页并逐页截屏'''
# 当前激活标签页为0
driver.switch_to.window(driver.window_handles[0])
for i in range(total_page):
    num = i + 1
    # 等待loading状态结束
    div_loading = driver.find_element(By.CSS_SELECTOR, 'div[class="loading"')
    while div_loading.is_displayed():
        print("waiting ...")
        time.sleep(1)
    # 浏览器全屏截图
    time.sleep(0.5)
    print("shot : %d / %d" % (num, total_page))
    shot_path = os.path.join(save_path, "shot_%d.png" % num)
    driver.save_screenshot(shot_path)
    # 锐化程序同步进行
    th_sharpen = threading.Thread(target=sharpen_main, args=[shot_path], daemon=True)
    th_sharpen.start()
    # 点击进入下一页
    ActionChains(driver).move_by_offset(100, 450).click().move_by_offset(-100, -450).perform()

print("shot-function finish")
driver.quit()
