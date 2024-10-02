'''
create: 2023.4.21
点击器

'''


import time
import pyautogui
import pynput.keyboard as pk

from utils_logger.log import logger_re as logger
from utils_screenshot.shot_func import ShotFunc
from utils_winsdk.winsdk_notification import WinsdkNotification


class AutoClick():
    def __init__(self, json_set={}) -> None:
        '''只有一个total_page是必须参数,其他都有预设值'''
        try:
            # x轴坐标
            self.pos_x = int(json_set["pos_x"])
            # y轴坐标
            self.pos_y = int(json_set["pos_y"])
            # 点击间隔
            self.sleep_time = int(json_set["sleep_time"])
        except Exception as e:
            logger.error("key error: %s" % e)
            return

        # 控制while循环退出
        self.run_flag = True

    def get_pos(self):
        '''获取当前坐标'''
        logger.info("press any key to record")
        def _press(key):
            mouseX, mouseY = pyautogui.position() 
            logger.debug("x : %d , y : %d" % (mouseX, mouseY))
            listener.stop()
        with pk.Listener(on_press=_press) as listener:
            listener.join()

    def __click(self):
        '''点击函数'''
        pyautogui.click(self.pos_x, self.pos_y)

    def __on_press(self, key):
        '''键盘触发'''
        logger.info("exit")
        self.run_flag = False

    def run(self):
        '''开始处理'''

        logger.info("auto click start ...")
        logger.info("press any key to exit")

        listener = pk.Listener(on_press=self.__on_press)
        listener.start()

        count = 0
        while self.run_flag:
            count += 1
            self.__click()
            logger.info("click times : %d" % count)
            time.sleep(self.sleep_time)
