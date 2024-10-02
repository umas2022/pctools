'''
create: 2023.5.15
幻影坦克
'''

import os
from shutil import copyfile
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse
from utils_tools.traverse_copy import TVcopy

import sys,os
script_path =os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_path)
from mirage_white import build

class CopyMirage(TVcopy):
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
            TVcopy.__init__(self,self.path_in,self.path_out,self.path_log,self.if_count)
        except Exception as e:
            logger.error("key error: %s" % e)
            return

    def func_handle(self,full_in,full_out,jetzt):
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
        logger.info("copy mirage function start ...")
        logger.write("copy mirage")
        self.find_all(Traverse().get_first_file,self.func_handle)

