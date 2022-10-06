'''
create: 2022.9.19

图片压缩
'''

import os
from PIL import Image  # pip install pillow
from shutil import copyfile
from moviepy.editor import *  # pip install moviepy
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse


class ImgCompress():
    '''JustCopy + 图片压缩\n
    必要参数：path_in, path_out\n
    默认参数：max_size(3072)'''

    def __init__(self,path_in,path_out, path_log="", maxSizeKB=3072) -> None:
        self.path_in = str(path_in).replace("\\", "/")
        self.path_out = str(path_out).replace("\\", "/")
        logger.raw_logger.set_path(str(path_log).replace("\\", "/"))
        # 图片尺寸上限
        self.maxSizeKB = maxSizeKB
        # 单次压缩系数
        self.cutCoefficient = 0.9
        # 默认处理的文件格式
        self.handleFormat = ["jpg", "JPG", "jpeg", "bmp", "BMP", "jpe", "JPEG"]
        # 需要转换的图片格式
        self.transFormat = ["png", "PNG"]

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
                logger.error("sp-ImgCut - COPY ERROR !!! :%s" % e)
                logger.error("file : %s" % methodPathIn)
                return "error"

    def __method_cut(self, methodPathIn, methodPathOut) -> None:
        '''图片处理方法：压缩'''
        imgSizeRaw = os.path.getsize(methodPathIn) / 1024
        img = Image.open(methodPathIn)
        imgSizeOut = imgSizeRaw
        try:
            while imgSizeOut > self.maxSizeKB:
                img = img.resize((int(img.size[0] * self.cutCoefficient), int(
                    img.size[1] * self.cutCoefficient)), Image.ANTIALIAS)
                img = img.convert('RGB')
                img.save(methodPathOut, quality=int(100 * self.cutCoefficient))
                imgSizeOut = os.path.getsize(methodPathOut) / 1024
                return "compress"
        except Exception as e:
            logger.error("sp-ImgCut - cut error !!! %s" % e)
            logger.error("file : %s" % methodPathIn)
            return "error"

    def __method_trans(self, methodPathIn, methodPathOut) -> None:
        '''图片处理方法：转换'''
        try:
            # 先以jpg保存，压缩后再改名为png
            imgPathOutJpg = methodPathOut.replace(
                "." + methodPathOut.split(".")[-1], ".jpg")
            img = Image.open(methodPathIn)
            img = img.convert('RGB')
            img.save(imgPathOutJpg)
            self.__method_cut(imgPathOutJpg, imgPathOutJpg)
            os.rename(imgPathOutJpg, methodPathOut)
            return "transform"
        except Exception as e:
            logger.error("sp-ImgCut - trans error !!! %s" % e)
            logger.error("file : %s" % methodPathIn)
            return "error"

    def __img_filter(self, methodPathIn, methodPathOut) -> str:
        '''处理方法分类器'''
        # 创建输出目录结构
        name = methodPathIn.split("/")[-1]
        suffix = methodPathOut.split(".")[-1]
        dir_out = methodPathOut.replace("/" + name, "")
        if not os.path.exists(dir_out):
            try:
                os.makedirs(dir_out)
            except Exception as e:
                logger.error("sp-ImgCut - MAKEDIR ERROR !!! :%s" % e)
                logger.error("file : %s" % dir_out)

        # 输出路径已存在格式在拷贝列表中的文件，或满足尺寸条件的图片
        if os.path.isfile(methodPathOut):
            imgSizeOut = os.path.getsize(methodPathOut) / 1024
            if imgSizeOut < self.maxSizeKB:
                return "pass"
            # 若已存在图片尺寸不满足条件，则删除该图片
            else:
                try:
                    if suffix in self.handleFormat or suffix in self.transFormat:
                        os.remove(methodPathOut)
                except Exception as e:
                    logger.error(
                        "error-001 : ImgCut - remove png error !!! :%s" % e)
                    logger.error("path : %s" % dir_out)

        imgSizeRaw = os.path.getsize(methodPathIn) / 1024
        # 原图尺寸满足，直接拷贝
        if imgSizeRaw < self.maxSizeKB:
            return self.__method_copy(methodPathIn, methodPathOut)
        # 转换列表
        elif suffix in self.transFormat:
            return self.__method_trans(methodPathIn, methodPathOut)
        # 压缩列表
        elif suffix in self.handleFormat:
            return self.__method_cut(methodPathIn, methodPathOut)
        # 其他格式
        else:
            pass

    def run(self):
        '''开始处理'''
        logger.info("image compress function start ...")
        logger.write("image compress")
        # 计数
        total = 0
        for full_in in Traverse().get_file(self.path_in):
            if full_in.split(".")[-1] in self.handleFormat or full_in.split(".")[-1] in self.transFormat:
                total += 1
                name = full_in.replace("\\", "/").split("/")[-1]
                logger.info("counting : %d\t%s" % (total, name))
        logger.write("total : %d\n" % total)
        # 开始
        jetzt = 0
        for full_in in Traverse().get_file(self.path_in):
            full_in = full_in.replace("\\", "/")
            # 单文件名
            name = full_in.split("/")[-1]
            # 对root的相对路径
            name_upper_dir = full_in.replace(self.path_in + "/", "")
            # 完整输出路径
            full_out = os.path.join(self.path_out, name_upper_dir).replace("\\", "/")
            state = self.__img_filter(full_in, full_out)
            if state:
                jetzt +=1
                logger.info("%s\t%d/%d\t%s" % (state, jetzt, total, full_in))
