'''
create: 2023.3.29
漫画截图翻译


'''


import os
import subprocess
import cv2
import numpy as np
import pyautogui
from utils_logger.log import logger_re as logger
from utils_screenshot.shot_func import ShotFunc
from PIL import ImageGrab
from PIL import Image
import cv2
import pytesseract  # pip install pytesseract # 需要配置pytesseract路径
from deep_translator import GoogleTranslator  # pip install deep-translator


class AutoTrans():
    '''漫画截图翻译'''

    def __init__(self, json_set={}) -> None:
        '''带*号标记为必填项'''
        try:
            # * 目标路径
            self.save_path = os.path.normpath(json_set['save_path'])
            # 日志路径
            self.path_log = os.path.normpath(json_set['path_log']) if "path_log" in json_set else ""
            self.path_log = "" if self.path_log == "." else self.path_log
            logger.raw_logger.set_path(self.path_log)
            # * 目标语言
            self.target = json_set['target']
            # * 翻译语言
            self.translate = json_set['translate']
        except Exception as e:
            logger.error("key error: %s" % e)
            return
        # 截图文件名和路径
        self.jpg_name = "shot.jpg"
        self.jpg_path = os.path.join(self.save_path, self.jpg_name)


    def startShot(self):
        '''开始截图'''
        # 获取屏幕截图
        screenshot = np.array(pyautogui.screenshot())
        # 将RGB模式的屏幕截图转换为BGR模式
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)    

        # 创建全屏窗口
        cv2.namedWindow("Screenshot", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Screenshot", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
        # 显示屏幕截图
        cv2.imshow("Screenshot", screenshot)

        # 等待用户选择区域
        region = cv2.selectROI("Screenshot", screenshot, fromCenter=False, showCrosshair=True)
        cv2.destroyAllWindows()

        # 获取用户选择的区域
        left, top, width, height = region

        # 在屏幕截图上绘制矩形框
        cv2.rectangle(screenshot, (left, top), (left + width, top + height), (0, 255, 0), 2)

        # 截取用户选择的区域
        screenshot = screenshot[top:top+height, left:left+width]

        # 保存截图
        cv2.imwrite(self.jpg_path, screenshot)

    def ocr_trans(self):
        '''ocr和翻译主函数'''
        try:
            img = Image.open(self.jpg_path)
            text = pytesseract.image_to_string(img, lang=self.target)
            text = str(text).replace(" ", "").replace("\n", "")
            logger.info("target: %s" % text)
            if self.target in ["jpn", "jpn_vert"]:
                translated = GoogleTranslator(source='ja', target=self.translate).translate(text=text)  # Chinese translation
                logger.info("translate: %s" % translated)
            else:
                logger.error("unexpected target : %s" % self.target)
        except Exception as e:
            logger.error("translate error, $s" % e)

    def run(self):
        '''开始处理'''
        logger.info("auto trans function start ...")
        logger.write("auto trans")
        self.startShot()
        self.ocr_trans()
