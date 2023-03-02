'''
create: 2023.2.25
窗口截图


'''


import os
import subprocess

from utils_logger.log import logger_re as logger
from utils_screenshot.shot_func import ShotFunc


class AutoCmd():
    def __init__(self, cmd_text="", json_set={}) -> None:
        # 命令文本
        self.cmd_text = str(cmd_text)
        try:
            self.cmd_text = str(json_set["cmd_text"])
        except Exception as e:
            logger.error("key error: %s" % e)
            return
        

    def run(self):
        '''开始处理'''
        try:
            os.system(self.cmd_text)
        except Exception as e:
            logger.error(e)
