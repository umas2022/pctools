'''
create: 2023.5.15
幻影坦克
'''

import os
from shutil import copyfile
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse

import sys,os
script_path =os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_path)
from mirage_white import build

class CopyMirage():
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
        except Exception as e:
            logger.error("key error: %s" % e)
            return

    def __copy_mirage(self,full_in,full_out,jetzt):
        '''幻影坦克生成主函数'''
        full_out = full_out.split(".")
        full_out[-1] = "png"
        full_out = ".".join(full_out)
        try:
            build(full_in,full_out)
            return "success"
        except Exception as e:
            logger.error("error ! %s" %e)
            return "error"

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
            state = self.__copy_mirage(full_in, full_out, jetzt)
            logger.info("%s\t%d/%d\t%s" % (state, jetzt, total, full_in))
