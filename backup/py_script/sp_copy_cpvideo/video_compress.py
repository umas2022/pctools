'''
create: 2022.9.19

视频压缩
目前只对比特率进行压缩, 尚未实现尺寸的压缩
- 程序运行时moviepy在程序目录下生成临时视频文件, 需优化
'''

import os
from PIL import Image  # pip install pillow
from shutil import copyfile
from moviepy.editor import *  # pip install moviepy
import ffmpeg  # pip install ffmpeg-python, 需要windows中配置好环境变量
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse
from utils_tools.traverse_copy import TVcopy


class VideoCompress(TVcopy):
    def method_name(self):
        return "video_compress"

    def __init__(self,json_set = {}) -> None:
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
            TVcopy.__init__(self,self.path_in,self.path_out,self.path_log,self.if_count)

            # 最大比特率(kbps)
            self.max_bit_kbps = int(json_set['max_bit_kbps'])  if "max_bit_kbps" in json_set else 10000
            # cpu占用量（6核cpu, thread=3, 占用率50%）
            self.cpu_thread = int(json_set['cpu_thread']) if "cpu_thread" in json_set else 3

            # 容许系数(倍率范围内都被视为满足条件, 由于写入误差存在, 此系数建议>1.05)
            self.tolerance_factor = 1.2
            # 默认处理的文件格式
            self.handleFormat = ["mp4", "MP4", "wmv", "webm",
                             "ogv", "mkv", "m4v", "MTS", "mov", "avi"]
        except Exception as e:
            logger.error("key error: %s" % e)
            return
        

    def __method_copy(self, methodPathIn, methodPathOut) -> None:
        '''处理方法：直接拷贝'''
        if os.path.isfile(methodPathOut):
            return "exist"
        else:
            # 拷贝文件
            try:
                copyfile(methodPathIn, methodPathOut)
                return "copy"
            except Exception as e:
                logger.error("sp-VideoCompress - COPY ERROR !!! :%s" % e)
                logger.error("file : %s" % methodPathIn)
                return "error"

    def __method_compress(self, methodPathIn, methodPathOut) -> None:
        '''处理方法：压缩'''
        try:
            logger.info("compress target : %s" % methodPathIn)
            clip = VideoFileClip(methodPathIn)
            # 总比特率设定 1w kbps 实测质量较好, 6核cpu设定thread=3占用50%
            clip.write_videofile(methodPathOut, bitrate=str(
                self.max_bit_kbps * 1024), threads=self.cpu_thread)
            return "compress"
        except Exception as e:
            logger.error("sp-VideoCompress - compress error !!! %s" % e)
            logger.error("file : %s" % methodPathIn)
            return "error"

    def func_handle(self, methodPathIn, methodPathOut,jetzt) -> str:
        '''处理方法分类器'''
        # 创建输出目录结构
        name = methodPathIn.split("/")[-1]
        dir_out = methodPathOut.replace("/" + name, "")
        if not os.path.exists(dir_out):
            try:
                os.makedirs(dir_out)
            except Exception as e:
                logger.error("sp-VideoCompress - MAKEDIR ERROR !!! :%s" % e)
                logger.error("file : %s" % dir_out)

        # 状态：pass, 输出路径已存在目标文件
        if os.path.isfile(methodPathOut):
            try:
                probe = ffmpeg.probe(methodPathOut)
                bitrate = int(int(probe['format']['bit_rate']) / 1024)
                if bitrate < self.max_bit_kbps * self.tolerance_factor:
                    return "pass"
            except Exception as e:
                logger.error("sp-VideoCompress - exists file read error :%s" % e)
                logger.error("file : %s" % dir_out)
                return "error"

        # 状态：copy, 原文件已满足条件, 不处理直接拷贝
        try:
            probe = ffmpeg.probe(methodPathIn)
            bitrate = int(int(probe['format']['bit_rate']) / 1024)
            if bitrate < self.max_bit_kbps * self.tolerance_factor:
                return self.__method_copy(methodPathIn, methodPathOut)
        except Exception as e:
            logger.error("sp-VideoCompress - copy read file error :%s" % e)
            logger.error("file : %s" % dir_out)
            return "error"

        # 状态：compress, 其余情况进入压缩函数
        return self.__method_compress(methodPathIn, methodPathOut)

    def run(self):
        '''开始处理'''
        logger.info("video compress function start ...")
        logger.write("video compress")
        self.find_all(Traverse().get_file,self.func_handle)


