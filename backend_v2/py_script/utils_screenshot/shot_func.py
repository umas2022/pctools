'''
create: 2023.2.25
屏幕截图方法合集
'''

import sys
import subprocess
import threading
import skimage.metrics
import skimage.measure
import cv2  # pip install opencv-python
import win32gui  # pip install pypiwin32
from PyQt6.QtWidgets import QApplication  # pip install PyQT6

from utils_logger.log import logger_re as logger


class ShotFunc():
    '''截图方法合集,多次实例化会导致QApplication报警,建议只实例化一次'''
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        logger.debug("重复操作会触发QApplication重复实例化的warning,不影响使用(修不好了)")


    def hwnd_print_all(self) -> None:
        '''直接print所有窗口名和id'''
        hwnd_title = dict()
        def get_all_hwnd(hwnd, mouse):
            if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
        win32gui.EnumWindows(get_all_hwnd, 0)
        for h, t in hwnd_title.items():
            if t != "":
                print(h, t)


    def hwnd_yield_all(self) -> None:
        '''yield所有窗口名和id'''
        hwnd_title = dict()
        def get_all_hwnd(hwnd, mouse):
            if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
        win32gui.EnumWindows(get_all_hwnd, 0)
        for h, t in hwnd_title.items():
            if t != "":
                yield(h, t)


    def hwnd_match(self,keyword)->str:
        '''返回包含关键字的第一个目标句柄,匹配失败时返回空字符串'''
        for (win_id,win_title) in self.hwnd_yield_all():
            if keyword in win_title:
                return win_title
        return ""


    def shot_window(self,window: str, save_path: str) -> None:
        '''按窗口截图;window窗口名不存在时全屏截图;save_path包含图片名'''
        hwnd = win32gui.FindWindow(None, window)
        screen = QApplication.primaryScreen()
        img = screen.grabWindow(hwnd).toImage()
        img.save(save_path)


    def shot_window_cut(self,window: str, save_path: str, y1: int, y2: int, x1: int, x2: int):
        '''
        截图后剪裁
        '''
        self.shot_window(window, save_path)
        img = cv2.imread(save_path)
        croped = img[y1:y2, x1:x2]
        cv2.imwrite(save_path, croped)


    def compare_ssim(self,path_image1: str, path_image2: str, show_score=False) -> float:
        '''
        ssim对比两张图片的结构相似性(红、绿、蓝、灰度),返回相似度scor: 0 < score < 1
        '''
        imageA = cv2.imread(path_image1)
        imageB = cv2.imread(path_image2)
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        score_gray = skimage.metrics.structural_similarity(
            grayA, grayB, data_range=255)
        if show_score:
            print("SSIM gray: {}".format(score_gray))
        colorA = cv2.cvtColor(imageA, cv2.IMREAD_COLOR)
        blueA = colorA[:, :, 0]
        greenA = colorA[:, :, 1]
        redA = colorA[:, :, 2]
        colorB = cv2.cvtColor(imageB, cv2.IMREAD_COLOR)
        blueB = colorB[:, :, 0]
        greenB = colorB[:, :, 1]
        redB = colorB[:, :, 2]
        score_blue = skimage.metrics.structural_similarity(
            blueA, blueB, data_range=255)
        if show_score:
            print("SSIM blue: {}".format(score_blue))
        score_green = skimage.metrics.structural_similarity(
            greenA, greenB, data_range=255)
        if show_score:
            print("SSIM green: {}".format(score_green))
        score_red = skimage.metrics.structural_similarity(
            redA, redB, data_range=255)
        if show_score:
            print("SSIM red: {}".format(score_red))

        return min(score_gray, score_red, score_green, score_blue)