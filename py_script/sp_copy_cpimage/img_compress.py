'''
create: 2022.9.19

图片压缩
- 质量和尺寸双重压缩, 边界条件为图片占用空间
'''

import os
import time
from PIL import Image  # pip install pillow
from shutil import copyfile
from moviepy.editor import *  # pip install moviepy
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse
from utils_tools.traverse_copy import TVcopy


class ImgCompress(TVcopy):
    '''JustCopy + 图片压缩\n
    必要参数：path_in, path_out\n
    默认参数：max_size(3072)'''

    def __init__(self, json_set={}) -> None:
        try:
            # *输入路径
            self.path_in = os.path.normpath(json_set['path_in'])
            # *输出路径
            self.path_out = os.path.normpath(json_set['path_out'])
            # 日志路径(默认无)
            self.path_log = os.path.normpath(json_set['path_log']) if "path_log" in json_set else ""
            logger.set_path(str(self.path_log).replace("\\", "/"))
            # 程序控制:是否计数(默认True)
            self.if_count = bool(json_set['if_count']) if "if_count" in json_set else True
            TVcopy.__init__(self, self.path_in, self.path_out, self.path_log, self.if_count)

            # 图片尺寸上限
            self.max_size_kb = int(json_set['max_size_kb']) if "max_size_kb" in json_set else 3072

            # 单次压缩系数
            self.cutCoefficient = 0.9
            # 默认处理的文件格式
            self.handleFormat = ["jpg", "JPG", "jpeg", "bmp", "BMP", "jpe", "JPEG"]
            # 需要转换的图片格式
            self.transFormat = ["png", "PNG"]
        except Exception as e:
            logger.error("ImgCut - key error !!! : %s" % e)
            return

    def __method_copy(self, methodPathIn, methodPathOut) -> None:
        '''图片处理方法：直接拷贝'''
        if os.path.isfile(methodPathOut):
            return "pass"
        else:
            # 拷贝文件
            try:
                copyfile(methodPathIn, methodPathOut)
                return "copy"
            except Exception as e:
                logger.error("ImgCut - copy error !!! :%s" % e)
                logger.error("path : %s" % methodPathIn)
                return "error"

    def __method_cut(self, methodPathIn, methodPathOut) -> None:
        '''图片处理方法：压缩'''
        imgSizeRaw = os.path.getsize(methodPathIn) / 1024
        img = Image.open(methodPathIn)
        imgSizeOut = imgSizeRaw
        try:
            # 依系数cutCoefficient循环压缩至满足要求
            while imgSizeOut > self.max_size_kb:
                img = img.resize((int(img.size[0] * self.cutCoefficient), int(
                    img.size[1] * self.cutCoefficient)), Image.ANTIALIAS)
                img = img.convert('RGB')
                img.save(methodPathOut, quality=int(100 * self.cutCoefficient))
                imgSizeOut = os.path.getsize(methodPathOut) / 1024
            return "compress"
        except Exception as e:
            logger.error("ImgCut - cut error !!! %s" % e)
            logger.error("path : %s" % methodPathIn)
            return "error"

    def __method_trans(self, methodPathIn, methodPathOut) -> None:
        '''图片处理方法：转换'''
        try:
            # 先以jpg保存
            imgPathOutJpg = methodPathOut.replace("." + methodPathOut.split(".")[-1], ".jpg")
            img = Image.open(methodPathIn)
            img = img.convert('RGB')
            img.save(imgPathOutJpg)
            # 压缩后再改名为png
            self.__method_cut(imgPathOutJpg, imgPathOutJpg)
            if self.path_in == self.path_out:
                os.remove(methodPathOut)
            os.rename(imgPathOutJpg, methodPathOut)
            return "png2jpg"
        except Exception as e:
            logger.error("ImgCut - trans error !!! %s" % e)
            logger.error("path : %s" % methodPathIn)
            return "error"

    def func_handle(self, methodPathIn, methodPathOut, jetzt) -> str:
        '''处理方法分类器'''
        # 创建输出目录结构
        suffix = methodPathOut.split(".")[-1]
        dir_out = os.path.split(methodPathOut)[0]
        if not os.path.exists(dir_out):
            try:
                os.makedirs(dir_out)
            except Exception as e:
                logger.error("ImgCut - makedir error !!! :%s" % e)
                logger.error("path : %s" % dir_out)

        # 输出路径已存在格式在拷贝列表中的文件, 或满足尺寸条件的图片
        if os.path.isfile(methodPathOut):
            imgSizeOut = os.path.getsize(methodPathOut) / 1024
            if imgSizeOut < self.max_size_kb:
                return "pass"
            # 若已存在图片尺寸不满足条件, 则删除该图片
            else:
                try:
                    if suffix in self.handleFormat or suffix in self.transFormat:
                        if not self.path_in == self.path_out:
                            os.remove(methodPathOut)
                except Exception as e:
                    logger.error("ImgCut - remove png error !!! :%s" % e)
                    logger.error("path : %s" % dir_out)

        try:
            imgSizeRaw = os.path.getsize(methodPathIn) / 1024
            # 原图尺寸满足, 直接拷贝
            if imgSizeRaw < self.max_size_kb:
                return self.__method_copy(methodPathIn, methodPathOut)
            # 转换列表
            elif suffix in self.transFormat:
                return self.__method_trans(methodPathIn, methodPathOut)
            # 压缩列表
            elif suffix in self.handleFormat:
                return self.__method_cut(methodPathIn, methodPathOut)
            # 其他格式
            else:
                return "skip"
        except Exception as err:
            logger.error("ImgCut - getsize error !!! : %s" % err)
            logger.error("path : %s" % methodPathIn)

    def run(self):
        '''开始处理'''
        logger.info("image compress function start ...")
        logger.write("image compress")
        self.find_all(Traverse().get_file, self.func_handle)

