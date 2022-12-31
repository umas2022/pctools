'''
create: 2022.12.4
bookwalker漫画《妖精森林的小不点》爬虫

思路:
    1. 手动启动chrome打开debug端口,转交selenium
    2. 代码截图,点击进入下一页,根据viewport0的显示状态判断点击是否成功
    3. 图片锐化(+信息删除)和截图双线程同步进行(jpg节省空间)
    4. 截图保存后检查文件大小,小于设定值的截图被判断为loading页,重新截图
问题:
    1.截图清晰度受屏幕分辨率影响,质量较低;网页截图比平板截屏质量差
    2.对div.loading状态的判断不完全可靠,检查图片大小的方法也可能存在误判
    3.保存截图会花费约0.5s,使用多线程并行运行时报错
    4.ActionChains的点击动作会花费约0.5s,需要优化

chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\\p-data\\chrome_temp"

https://bookwalker.jp/bookshelf1/

'''


# 总页数(设为1截取单页)
total_page = 1248
# 起始页码(截图保存命名用)
current_page = 1
# 图片保存位置(路径下不要有其他图片)
save_path = r"D:\s-workspace\crawler_save"
# 图片锐化系数(1为原图,实测2效果还行)
sharp_factor = 2
# debug模式chrome数据位置(用于chrome的脚本启动)
chrome_path = r"D:\\p-data\\chrome_temp"
# chrome driver位置(注意要和chrome版本一致)
# https://chromedriver.chromium.org/downloads
driver_path = r"D:\p-tools\chromedriver\chromedriver108.exe"
# chrome已经手动ready,脚本不再启动chrome
chrome_ready = True
# 重新截图大小(KB)(不同截图环境loading页大小不相同)
reshot_size = 200
# 截图/点击,重试次数上限
retry_times = 8


import time
import threading
import logging
import os
import sys
import copy
# 删除图片信息
import piexif  # pip install piexif
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
time_start = time.time()

'''设置logger'''
logger = logging.getLogger('py_demo')
# 控制台输出级别
logger.setLevel(level=logging.DEBUG)
# 控制台输出格式
formatter_console = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter_console)
logger.addHandler(stream_handler)
# 文件输出格式
log_path = r"./"
time_prefix = time.strftime("%Y-%m-%d_%H.%M", time.localtime())
log_file = os.path.join(log_path, time_prefix + '.log')
formatter_file = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setFormatter(formatter_file)
# 文件输出级别
file_handler.setLevel(level=logging.WARNING)
logger.addHandler(file_handler)


def sharpen_main(shot_path):
    '''子线程:图片锐化+删除信息主函数'''
    shot_path_list = shot_path.split("/")
    img = Image.open(shot_path)
    enhancer = ImageEnhance.Sharpness(img)
    im_s = enhancer.enhance(sharp_factor)
    shot_path_list[-1] = shot_path_list[-1].replace("shot", "sharp")
    sharp_path = "/".join(shot_path_list)
    # jpg节省点空间
    im_s = im_s.convert('RGB')
    sharp_path = sharp_path.replace(".png", ".jpg")
    im_s.save(sharp_path)
    os.remove(shot_path)
    # 删除信息(其实正常截图本来就不含信息)
    piexif.remove(sharp_path)


'''实例化浏览器'''
if not chrome_ready:
    os.system('chrome.exe --remote-debugging-port=9222 --user-data-dir="%s"' % chrome_path)
    wait_here = input("make sure chrome is ready and press enter to continue ...")
option = ChromeOptions()
option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
# 实例化谷歌
driver = webdriver.Chrome(executable_path=driver_path, options=option)
# 窗口尺寸不能超过显示尺寸,只能考虑找一台高分辨率显示器或者多屏拼接
# driver.set_window_size(1080,1920)

'''进入漫画页并逐页截屏'''
# 当前激活标签页为0
driver.switch_to.window(driver.window_handles[0])
viewport_before = driver.find_element(By.CSS_SELECTOR, 'div[id="viewport0"').is_displayed()
for i in range(total_page):
    num = i + current_page
    # 等待loading状态结束(对loading的判断并不完全可靠,建议翻页后的wait_time>0.5s)
    div_loading = driver.find_element(By.CSS_SELECTOR, 'div[class="loading"')
    while div_loading.is_displayed():
        logger.info("loading ...")
        time.sleep(1)
    # 浏览器全屏截图(截图动作占用约0.5s,并行报错暂未解决)
    time_cost = int(time.time() - time_start)
    time_left = int(time_cost / (i + 1) * (total_page - i - 1))
    logger.info("shot : %d / %d , page : %d, time-left : %d s" % (i + 1, total_page, num, time_left))
    shot_path = os.path.join(save_path, "shot_%d.png" % num)
    driver.save_screenshot(shot_path)
    # 检查截图大小,小于设定值为loading页,重新截图
    shot_retry = 0
    while True:
        shot_retry += 1
        shot_size = os.path.getsize(shot_path) / 1024
        if shot_size > reshot_size:
            break
        if shot_retry > retry_times:
            logger.warning("shot %d times retry! file: %s" % (retry_times, shot_path))
            break
        time.sleep(1)
        logger.info("shot retry %d ..." % shot_retry)
        driver.save_screenshot(shot_path)
    # 锐化程序并行进行
    th = threading.Thread(target=sharpen_main, args=[shot_path], daemon=True)
    th.start()
    # 点击进入下一页(即使设置了duration,这个动作仍然会占用约0.5s的时间)
    click_retry = 0
    while True:
        click_retry += 1
        ActionChains(driver, duration=10).move_by_offset(100, 450).click().move_by_offset(-100, -450).perform()
        time.sleep(0.5)
        viewport_now = driver.find_element(By.CSS_SELECTOR, 'div[id="viewport0"').is_displayed()
        if viewport_now != viewport_before:
            break
        else:
            time.sleep(1)
            viewport_now = driver.find_element(By.CSS_SELECTOR, 'div[id="viewport0"').is_displayed()
            if viewport_now != viewport_before:
                break
            logger.info("click retry %d ..." % click_retry)
            if click_retry > retry_times:
                logger.error("click %d times retry!" % retry_times)
                exit(1)

    viewport_before = viewport_now
    # wait_here = input("go >>")

logger.info("shot-function finish")
driver.quit()
