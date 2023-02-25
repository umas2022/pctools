'''
create: 2023.2.25
窗口截图


'''


import os
import time

from utils_logger.log import logger_re as logger
from utils_screenshot.shot_func import ShotFunc


class AutoShot():
    def __init__(self, save_path="", img_name="", win_name="", json_set={}) -> None:
        '''只有一个total_page是必须参数,其他都有预设值'''
        # 缓存路径和名称(用以保存临时截图文件)
        self.save_path = os.path.normpath(str(save_path))
        self.img_name = str(img_name)
        # 目标窗口名,支持字符串匹配,输入关键字即可
        self.win_name = str(win_name)

        try:
            self.save_path = os.path.normpath(str(json_set["save_path"]))
            self.img_name = str(json_set["img_name"]) if not "img_name" == "" else "shot.jpg"
            self.win_name = str(json_set["win_name"])
        except Exception as e:
            logger.error("key error: %s" % e)
            return

        self.sf = ShotFunc()
        self.hwnd = ""
        self.img_path = os.path.normpath(os.path.join(self.save_path, self.img_name))

    def __shot(self) -> float:
        if os.path.isfile(self.img_path):
            os.remove(self.img_path)
        self.sf.shot_window(self.hwnd, self.img_path)

    def get_hwnd(self) -> None:
        '''获取所有窗口句柄'''
        for (win_id, win_name) in self.sf.hwnd_yield_all():
            logger.info("[ %s , %s ]" % (str(win_id), win_name))

    def run(self):
        '''开始处理'''
        self.hwnd = self.sf.hwnd_match(self.win_name)
        if self.hwnd == "":
            logger.error("window not found : %s" % self.win_name)
            return
        self.__shot()
        logger.info("done")
