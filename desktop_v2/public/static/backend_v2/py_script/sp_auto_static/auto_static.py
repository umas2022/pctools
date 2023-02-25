'''
create: 2023.2.25
检测窗口变化


'''


import os
import time

from utils_logger.log import logger_re as logger
from utils_screenshot.shot_func import ShotFunc
from utils_winsdk.winsdk_notification import WinsdkNotification


class AutoStatic():
    def __init__(self, path_cash="", win_name="", interval_time=1, json_set={}) -> None:
        '''只有一个total_page是必须参数,其他都有预设值'''
        # 缓存路径(用以保存临时截图文件)
        self.path_cash = os.path.normpath(str(path_cash))
        # 目标窗口名,支持字符串匹配,输入关键字即可
        self.win_name = str(win_name)
        # 检测时间间隔
        self.itv_time = int(interval_time)

        try:
            self.path_cash = os.path.normpath(str(json_set["path_cash"]))
            self.win_name = str(json_set["win_name"])
            self.itv_time = int(json_set["interval_time"])
        except Exception as e:
            logger.error("key error: %s" % e)
            return

        # 相似度阈值
        self.__grenze = 0.85
        # 重试检测时间,默认为3倍正常间隔
        self.__recheck_time = 3 * self.itv_time

        self.sf = ShotFunc()
        self.hwnd = ""
        self.s1_path = os.path.normpath(os.path.join(self.path_cash, "s1.jpg"))
        self.s2_path = os.path.normpath(os.path.join(self.path_cash, "s2.jpg"))

    def __two_shot(self) -> float:
        '''前后两次截图返回相似度,如果目录下已经存在s1.jpg和s2.jpg则保留s2并重命名为s1'''
        if  os.path.isfile(self.s2_path):
            if  os.path.isfile(self.s1_path):
                os.remove(self.s1_path)
            os.rename(self.s2_path, self.s1_path)
            self.sf.shot_window(self.hwnd, self.s2_path)
            time.sleep(self.itv_time)
        else:
            self.sf.shot_window(self.hwnd, self.s1_path)
            time.sleep(self.itv_time)
            self.sf.shot_window(self.hwnd, self.s2_path)
        return self.sf.compare_ssim(self.s1_path, self.s2_path)

    def __recheck(self) -> bool:
        '''检测到重复图片,延长等待时间并重新检测'''
        logger.info("inactivity detected, recheck ...")
        time.sleep(self.__recheck_time)
        return self.__two_shot()

    def run(self):
        '''开始处理'''
        if  os.path.isfile(self.s1_path):
            os.remove(self.s1_path)
        if  os.path.isfile(self.s2_path):
            os.remove(self.s2_path)
        
        self.hwnd = self.sf.hwnd_match(self.win_name)
        if self.hwnd == "":
            logger.error("window not found : %s" % self.win_name)
            return
        while True:
            ssim_score = self.__two_shot()
            logger.info("score: %.2f" % ssim_score)
            if ssim_score > self.__grenze:
                if self.__recheck() > self.__grenze:
                    break

        WinsdkNotification().wn_show("%s finish" % self.win_name, "enjoy yourself")
        logger.info("done")
