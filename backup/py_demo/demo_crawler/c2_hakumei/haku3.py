'''
create: 2022.12.4
bookwalker漫画《妖精森林的小不点》爬虫
思路:去除自动化功能,手动启动chrome打开debug端口,转交selenium,代码仅执行截图,两块显示器上下拼接扩大网页显示范围,图片锐化和截图双线程同步进行
问题:1.截图清晰度受屏幕分辨率影响,质量较低;网页截图比平板截屏质量差
    2.对loading状态的判断不完全可靠,偶尔会截到loading页
        - 一种可行的检验方法:loading页截下来只有36K,一般正常截图>1M(也可能有抽象白页<200k存在)
    3.保存截图会花费约0.5s,使用多线程并行运行时报错
    4.ActionChains的点击动作会花费约0.5s,需要优化

chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\\p-data\\chrome_temp"

https://bookwalker.jp/bookshelf1/

'''


# 总页数(设为1截取单页)
total_page = 1
# 起始页码(截图保存命名用)
current_page = 744
# 图片保存位置(路径下不要有其他图片)
save_path = r"D:\s-workspace\crawler_save"
# 图片锐化系数(1为原图,实测2效果还行)
sharp_factor = 2
# debug模式chrome数据位置(用于chrome的脚本启动)
chrome_path = r"D:\\p-data\\chrome_temp"
# chrome已经手动ready,脚本不再启动chrome
chrome_ready = True

import time
import threading
import os
import sys
import copy
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
    '''子线程:锐化主函数'''
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
    num = i + current_page
    # 等待loading状态结束(对loading的判断并不完全可靠,建议翻页后的wait_time>0.5s)
    div_loading = driver.find_element(By.CSS_SELECTOR, 'div[class="loading"')
    while div_loading.is_displayed():
        print("waiting ...")
        time.sleep(1)
    # 浏览器全屏截图(截图动作占用约0.5s,并行报错暂未解决)
    print("shot : %d / %d , page : %d" % (i + 1, total_page, num))
    shot_path = os.path.join(save_path, "shot_%d.png" % num)
    driver.save_screenshot(shot_path)
    # 锐化程序并行进行
    th = threading.Thread(target=sharpen_main, args=[shot_path], daemon=True)
    th.start()
    # 点击进入下一页(即使设置了duration,这个动作仍然会占用约0.5s的时间)
    ActionChains(driver, duration=10).move_by_offset(100, 450).click().move_by_offset(-100, -450).perform()
    time.sleep(0.5)

print("shot-function finish")
driver.quit()
