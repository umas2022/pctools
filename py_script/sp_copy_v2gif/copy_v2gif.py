'''
create: 2023.4.19
拷贝拆分,目标只有输入第一级目录下的文件,没有deep参数
'''

import os
from shutil import copyfile
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse
from moviepy.editor import VideoFileClip  # pip install moviepy


class Video2Gif():
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

            # 处理列表
            self.handel_list = ["mp4"]
            # moviepy参数,帧率
            self.fps = int(json_set['fps']) if "fps" in json_set else 10
            # moviepy参数,宽高
            self.size_w = int(json_set['size_w']) if "size_w" in json_set and not json_set['size_w']==""  else 0
            self.size_h = int(json_set['size_h']) if "size_h" in json_set and not json_set['size_h']=="" else 0

        except Exception as e:
            logger.error("key error: %s" % e)
            return

    def __copy_filter(self, methodPathIn, methodPathOut, jetzt):
        '''处理方法：视频转gif'''
        root_dir = os.path.split(methodPathOut)[0]
        root_name = os.path.split(methodPathOut)[1]

        ext = methodPathIn.split(".")[-1]
        if not ext in self.handel_list:
            return "pass"

        # 拼接输出路径
        methodPathOut = methodPathOut.split(".")
        methodPathOut[-1] = "gif"
        methodPathOut = ".".join(methodPathOut)

        # 开始转换
        video = VideoFileClip(methodPathIn)
        if self.size_h*self.size_w :
            video.write_gif(methodPathOut, fps=self.fps, resize=(self.size_w, self.size_h))
        else:
            video.write_gif(methodPathOut, fps=self.fps)
        return "v2gif"

    def run(self):
        '''开始处理'''
        logger.info("copy split function start ...")
        logger.write("copy split")
        # 计数
        total = 0
        if self.if_count:
            for full_in in Traverse().get_first_file(self.path_in):
                total += 1
                name = full_in.replace("\\", "/").split("/")[-1]
                logger.info("counting : %d\t%s" % (total, name))
            logger.write("total : %d\n" % total)
        else:
            logger.info("skip count ...")
        # 开始
        jetzt = 0
        for full_in in Traverse().get_first_file(self.path_in):
            jetzt += 1
            full_in = os.path.normpath(full_in)
            # 单文件名
            name = os.path.split(full_in)[-1]
            # 对root的相对路径
            name_upper_dir = os.path.relpath(full_in, self.path_in)
            # 完整输出路径
            full_out = os.path.normpath(os.path.join(self.path_out, name_upper_dir))
            state = self.__copy_filter(full_in, full_out, jetzt)
            logger.info("%s\t%d/%d\t%s" % (state, jetzt, total, full_in))
