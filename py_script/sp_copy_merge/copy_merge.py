'''
create: 2022.9.20

多级目录扁平至单级, 文件名合并目录名
'''

import os
from shutil import copyfile
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse
from utils_tools.traverse_copy import TVcopy


class CopyMerge(TVcopy):
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
            # 内层合并
            self.if_inner = bool(json_set['if_inner']) if "if_inner" in json_set else False
        except Exception as e:
            logger.error("key error: %s" % e)
            return
        

    def func_handle(self, methodPathIn, methodPathOut,jetzt):
        '''处理方法：拷贝合并'''
        relpath = os.path.relpath(methodPathIn,self.path_in)
        new_name = ".".join(relpath.split(os.sep))
        full_out = os.path.normpath(os.path.join(self.path_out, new_name)) 

        # 创建目录结构
        if not os.path.exists(self.path_out):
            try:
                os.makedirs(self.path_out)
            except Exception as e:
                logger.error("ToOne - MAKEDIR ERROR !!! :%s" % e)
                logger.error("DIR : %s" % self.path_out)

        # 拷贝文件
        if os.path.isfile(full_out):
            return "pass"
        else:
            try:
                copyfile(methodPathIn, full_out)
                return "copy"
            except Exception as e:
                logger.error("ToOne - COPY ERROR !!! :%s" % e)
                logger.error("DIR : %s" % methodPathIn)
                return "error"


    def run(self):
        '''开始处理'''
        logger.info("copy merge function start ...")
        logger.write("copy merge")
        if not self.if_inner:
            self.find_all(Traverse().get_file,self.func_handle)
        else:
            ori_path_in = self.path_in
            ori_path_out = self.path_out
            for first_dir in Traverse().get_first_dir(self.path_in):
                self.path_in = first_dir
                self.path_out = os.path.join(ori_path_out,os.path.relpath(first_dir,ori_path_in)) 
                self.find_all(Traverse().get_file,self.func_handle)
            


