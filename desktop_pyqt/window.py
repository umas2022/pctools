from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from skimage.metrics import structural_similarity
from cv2 import imread, cvtColor, COLOR_BGR2GRAY
from difflib import SequenceMatcher
from traceback import format_exc
import time
import pyperclip
from PIL import Image, ImageDraw, ImageFont, ImageGrab



IMAGE_PATH = "./config/image.jpg"
DRAW_PATH = "./config/draw.jpg"
FONT_PATH = "./config/other/华康方圆体W7.TTC"


# 翻译处理线程
class TranslaterProcess(QThread) :

    display_signal = pyqtSignal(str, str)
    draw_image_signal = pyqtSignal(bool)

    def __init__(self, object, trans_type) :

        super(TranslaterProcess, self).__init__()
        self.object = object
        self.trans_type = trans_type
        self.logger = object.logger


    # 获取图片颜色
    def getImageColor(self, image, coordinate) :

        try :
            region = image.crop(coordinate)
            color_dict = {}
            for i in region.getdata():
                if i not in color_dict:
                    color_dict[i] = 0
                color_dict[i] += 1
            color_dict = sorted(color_dict.items(), key=lambda x: x[1], reverse=True)
            if color_dict :
                # 避免过暗的背景色
                r = color_dict[0][0][0]
                g = color_dict[0][0][1]
                b = color_dict[0][0][2]
                if (r + g + b) / 3 < 20 :
                    return (255, 255, 255)
                else :
                    return color_dict[0][0]
            else :
                return (255, 255, 255)
        except Exception :
            return (255, 255, 255)


    # 竖排-气泡框抠字
    def drawRectMD(self, ocr_result, words) :

        for index, word in enumerate(words.split("\n")[:len(ocr_result)]) :
            ocr_result[index]["Words"] = word

        image = Image.open(IMAGE_PATH)
        coordinate = (0, 0, image.width, image.height)
        base_color = self.getImageColor(image, coordinate)
        font_color = (255-base_color[0], 255-base_color[1], 255-base_color[2])
        draw = ImageDraw.Draw(image)

        for val in ocr_result :
            setFont = ImageFont.truetype(FONT_PATH, val["WordWidth"])
            x1 = int(val["Coordinate"]["UpperLeft"][0])
            y1 = int(val["Coordinate"]["UpperLeft"][1])
            x2 = int(val["Coordinate"]["LowerRight"][0])
            y2 = int(val["Coordinate"]["LowerRight"][1])
            h = int(val["Coordinate"]["LowerLeft"][1] - val["Coordinate"]["UpperLeft"][1])

            # 获取文字区域基色并涂色
            draw.rectangle((x1, y1, x2, y2), fill=base_color)

            # 取平均字高字宽
            width_sum, height_sum, height_max = 0, 0, 0
            for char in val["Words"] :
                width, height = draw.textsize(char, setFont)
                width_sum += width
                height_sum += height
                if height > height_max :
                    height_max = height
            width = round(width_sum/len(val["Words"]))

            text = ""
            sum_height = 0
            x = x2 - width
            for char in val["Words"] :
                text += char + "\n"
                sum_height += height_max
                if sum_height + height_max > h :
                    draw.text((x, y1), text, fill=font_color, font=setFont, direction=None)
                    text = ""
                    sum_height = 0
                    x = x - width - 5
                elif char == val["Words"][-1] :
                    draw.text((x, y1), text, fill=font_color, font=setFont, direction=None)

        image.save(DRAW_PATH)
        self.draw_image_signal.emit(True)


    # 横排-气泡框抠字
    def drawRectTD(self, ocr_result, words):

        for index, word in enumerate(words.split("\n")[:len(ocr_result)]) :
            ocr_result[index]["Words"] = word

        image = Image.open(IMAGE_PATH)
        coordinate = (0, 0, image.width, image.height)
        base_color = self.getImageColor(image, coordinate)
        font_color = (255-base_color[0], 255-base_color[1], 255-base_color[2])
        draw = ImageDraw.Draw(image)

        for val in ocr_result:
            setFont = ImageFont.truetype(FONT_PATH, val["WordWidth"])
            x1 = int(val["Coordinate"]["UpperLeft"][0])
            y1 = int(val["Coordinate"]["UpperLeft"][1])
            x2 = int(val["Coordinate"]["LowerRight"][0])
            y2 = int(val["Coordinate"]["LowerRight"][1])
            w = int(val["Coordinate"]["LowerRight"][0] - val["Coordinate"]["LowerLeft"][0])

            # 文字区域涂色
            draw.rectangle((x1, y1, x2, y2), fill=base_color)

            # 取平均字高字宽
            width_sum = 0
            for char in val["Words"]:
                width, _ = draw.textsize(char, setFont)
                width_sum += width
            width = round(width_sum / len(val["Words"]))

            text = ""
            sum_width = 0
            for char in val["Words"] :
                text += char
                sum_width += width
                if sum_width + width > w :
                    sum_width = 0
                    text += "\n"
            draw.text((x1, y1), text, fill=font_color, font=setFont, direction=None)

        image.save(DRAW_PATH)
        self.draw_image_signal.emit(True)


    def run(self) :

        result = ""

        # 公共翻译一
        if self.trans_type == "webdriver_1" :
            if self.object.translation_ui.webdriver1.open_sign :
                result = self.object.translation_ui.webdriver1.translater(self.object.translation_ui.original)
            else :
                result = "%s翻译: 我抽风啦, 请尝试重新翻译! 如果频繁出现, 建议直接注册使用私人翻译"%self.object.translation_ui.webdriver1.translater_map[self.object.translation_ui.webdriver1.web_type]

        # 公共翻译二
        elif self.trans_type == "webdriver_2" :
            if self.object.translation_ui.webdriver2.open_sign :
                result = self.object.translation_ui.webdriver2.translater(self.object.translation_ui.original)
            else :
                result = "%s翻译: 我抽风啦, 请尝试重新翻译! 如果频繁出现, 建议直接注册使用私人翻译"%self.object.translation_ui.webdriver2.translater_map[self.object.translation_ui.webdriver2.web_type]

        # 公共翻译三
        elif self.trans_type == "webdriver_3":
            if self.object.translation_ui.webdriver3.open_sign :
                result = self.object.translation_ui.webdriver3.translater(self.object.translation_ui.original)
            else:
                result = "%s翻译: 我抽风啦, 请尝试重新翻译! 如果频繁出现, 建议直接注册使用私人翻译" % self.object.translation_ui.webdriver3.translater_map[self.object.translation_ui.webdriver3.web_type]

        elif self.trans_type == "original" :
            result = self.object.translation_ui.original

        # 根据屏蔽词过滤
        for val in self.object.config["Filter"]:
            if not val[0]:
                continue
            result = result.replace(val[0], val[1])

        result = result.strip()
        self.display_signal.emit(result, self.trans_type)

        # 翻译结果帖字
        if self.object.config["drawImageUse"] \
                and not self.object.config["baiduOCR"] \
                and self.trans_type != "original" \
                and self.object.ocr_result :
            ocr_result = self.object.ocr_result
            self.object.ocr_result = None
            try :
                if self.object.config["showTranslateRow"] == "True" :
                    self.drawRectMD(ocr_result, result)
                else :
                    self.drawRectTD(ocr_result, result)
            except Exception :
                self.logger.error(format_exc())


# 翻译处理模块
class Translater(QThread) :

    # 清屏翻译框信号
    clear_text_sign = pyqtSignal(bool)
    # 隐藏范围窗信号
    hide_range_ui_sign = pyqtSignal(bool)

    def __init__(self, object) :

        super(Translater, self).__init__()
        self.object = object
        self.logger = object.logger

    # 截图
    def imageCut(self):

        # 范围框坐标
        x = self.object.range_ui.x()
        y = self.object.range_ui.y()
        w = self.object.range_ui.width()
        h = self.object.range_ui.height()

        # 隐藏范围框信号
        if self.object.config["drawImageUse"] \
                and not self.object.config["baiduOCR"] :
            self.hide_range_ui_sign.emit(False)
            # 确保已经隐藏了范围框才截图
            while True :
                if self.object.range_ui.isHidden() :
                    break

        screen = QApplication.primaryScreen()
        image = screen.grabWindow(QApplication.desktop().winId(), x, y, w, h)

        if self.object.config["drawImageUse"] \
            and not self.object.config["baiduOCR"] \
            and self.object.translation_ui.translate_mode :
            self.hide_range_ui_sign.emit(True)

        image.save(IMAGE_PATH)
        self.object.range = (x, y, w, h)


    # 判断图片相似度
    def compareImage(self, imageA, imageB):

        grayA = cvtColor(imageA, COLOR_BGR2GRAY)
        grayB = cvtColor(imageB, COLOR_BGR2GRAY)

        (score, diff) = structural_similarity(grayA, grayB, full=True)
        score = float(score) * 100

        return score


    # 判断原文相似度
    def getEqualRate(self, str1, str2):

        score = SequenceMatcher(None, str1, str2).quick_ratio()
        score = score* 100

        return score


    # 创建翻译线程
    def creatTranslaterThread(self, trans_type) :

        if self.object.translation_ui.thread_state == 0 :
            # 发送清屏信号
            self.clear_text_sign.emit(True)
            self.object.translation_ui.statusbar.showMessage("翻译中...")
            QApplication.processEvents()

        self.object.translation_ui.thread_state += 1
        thread = TranslaterProcess(self.object, trans_type)
        thread.display_signal.connect(self.object.translation_ui.display_text)
        thread.draw_image_signal.connect(self.object.range_ui.drawImage)
        thread.start()
        thread.wait()


    # 翻译主模块
    def translate(self) :

        # 如果还未选取范围就操作翻译
        if self.object.range_ui.x() == 0 and self.object.range_ui.y() == 0:
            self.clear_text_sign.emit(True)
            self.object.translation_ui.original = "还未选取翻译范围, 请先使用范围键框选要翻译的屏幕区域"
            # 关闭翻译界面自动开关
            if self.object.translation_ui.translate_mode == True :
                self.object.translation_ui.switch_button.mousePressEvent(1)
                self.object.translation_ui.switch_button.updateValue()
            return

        try:
            # 首次执行或手动模式下, 直接跳过图片相似度检测
            if not self.object.translation_ui.original or not self.object.translation_ui.translate_mode :
                self.imageCut()
            else :
                try :
                    # 范围框坐标
                    x = self.object.range_ui.x()
                    y = self.object.range_ui.y()
                    w = self.object.range_ui.width()
                    h = self.object.range_ui.height()
                    # 如果坐标相同才判断相似度
                    if (x, y, w, h) == self.object.range :
                        imageA = imread(IMAGE_PATH)
                        self.imageCut()
                        imageB = imread(IMAGE_PATH)
                        image_score = self.compareImage(imageA, imageB)
                        # 在自动模式下, 如果如果相似度过高则不检测
                        if (image_score > self.object.config["imageSimilarity"]):
                            return
                    else :
                        self.imageCut()
                except Exception as err :
                    if str(err) != "Input images must have the same dimensions." :
                        self.logger.error(format_exc())
                    # 如果判断相似度失败则直接截图
                    self.imageCut()

        except Exception :
            self.logger.error(format_exc())
            # 如果截图时出错
            self.clear_text_sign.emit(True)
            self.object.translation_ui.original = "截取范围时出错: %s"%format_exc()
            return

        # OCR开始时间
        ocr_start_time = time.time()



        # 记录OCR耗时
        self.object.translation_ui.ocr_time = time.time()-ocr_start_time

 

        # 如果检测不到文字则跳过
        if not original :
            return

        # 根据屏蔽词过滤
        for val in self.object.config["Filter"]:
            if not val[0]:
                continue
            original = original.replace(val[0], val[1])

        # 自动模式下文字和上一次一样则跳过
        if self.object.translation_ui.translate_mode and original == self.object.translation_ui.original :
            return

        # 在自动模式下, 如果如果文本相似度过高则不翻译
        if self.object.translation_ui.translate_mode :
            text_score = self.getEqualRate(original, self.object.translation_ui.original)
            if text_score > self.object.config["textSimilarity"] :
                return

        # 更新原文
        self.object.translation_ui.original = original





    def run(self) :

        # 手动翻译
        if not self.object.translation_ui.translate_mode :

            # 如果上一次翻译未结束则直接跳过
            if self.object.translation_ui.thread_state > 0 :
                return

            try :
                self.translate()
            except Exception:
                self.logger.error(format_exc())

        else :
            # 自动翻译
            self.object.translation_ui.auto_trans_exist = True

            while True :

                # 如果自动翻译被停止则退出循环
                if not self.object.translation_ui.translate_mode :
                    self.object.translation_ui.auto_trans_exist = False
                    break

                # 自动翻译暂停
                if self.object.translation_ui.stop_sign :
                    time.sleep(0.1)
                    continue

                # 如果上一次翻译未结束则直接跳过
                if self.object.translation_ui.thread_state > 0:
                    continue

                try :
                    self.translate()
                except Exception :
                    self.logger.error(format_exc())

                if self.object.config["onlineOCR"]:
                    time.sleep(self.object.config["translateSpeed"]-0.2)
                else:
                    time.sleep(self.object.config["translateSpeed"]-0.4)