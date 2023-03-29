'''
create: 2023.3.29
漫画截图翻译


'''


import os
import subprocess

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
        # 全屏截图句柄
        self.img = ""
        # 全屏截图鼠标位置
        self.point1 = (0, 0)
        self.point2 = (0, 0)
        # 当前图片坐标
        self.pos_save = [0, 0, 0, 0]

    def startShot(self):
        '''开始截图'''
        self.img = ImageGrab.grab()
        screen_path = os.path.join(self.save_path, "screen.jpg")
        self.img.save(screen_path)  # 全屏截图
        self.img = cv2.imread(screen_path)
        cv2.namedWindow("img_window")
        cv2.setMouseCallback("img_window", self.onMouse)
        cv2.imshow("img_window", self.img)
        cv2.moveWindow("img_window", 0, 0)
        cv2.waitKey(0)

        os.remove(screen_path)

    def onMouse(self, event, x, y, flags, param):
        '''回调-在cv2图片窗口中移动鼠标触发'''
        img2 = self.img.copy()

        if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
            self.pointt1 = (x, y)
            self.pos_save[0] = self.pointt1[0]
            self.pos_save[2] = self.pointt1[1]
            cv2.imshow("img_window", img2)

        elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):  # 左键按住拖曳
            cv2.rectangle(img2, self.pointt1, (x, y), (255, 0, 0), 4)
            cv2.imshow("img_window", img2)

        elif event == cv2.EVENT_LBUTTONUP:  # 左键松开
            self.pointt2 = (x, y)
            self.pos_save[1] = self.pointt2[0]
            self.pos_save[3] = self.pointt2[1]

            cv2.rectangle(img2, self.pointt1, self.pointt2, (255, 0, 0), 4)
            cv2.imshow("img_window", img2)
            min_x = min(self.pointt1[0], self.pointt2[0])
            min_y = min(self.pointt1[1], self.pointt2[1])
            width = abs(self.pointt1[0] - self.pointt2[0])
            height = abs(self.pointt1[1] - self.pointt2[1])
            global cut_img
            cut_img = self.img[min_y:min_y + height, min_x:min_x + width]
            self.jpg_path = os.path.join(self.save_path, self.jpg_name)
            cv2.imwrite(self.jpg_path, cut_img)
            cv2.destroyAllWindows()

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
