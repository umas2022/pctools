'''
create: 2022.9.20

图片压缩
'''

import os
from shutil import copyfile
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse


class CopyMerge():
    def __init__(self, path_in, path_out) -> None:
        self.path_in = path_in.replace("\\", "/")
        self.path_out = path_out.replace("\\", "/")

    def __method_merge(self, methodPathIn, methodPathOut):
        '''处理方法：拷贝合并'''
        name = methodPathIn.split("/")[-1]
        name_upper_dir = methodPathIn.replace(self.path_in + "/", "")
        new_name = ".".join(name_upper_dir.split("/"))
        full_out = os.path.join(self.path_out, new_name).replace("\\", "/")

        if not os.path.exists(self.path_out):
            try:
                os.makedirs(self.path_out)
            except Exception as e:
                logger.error("ToOne - MAKEDIR ERROR !!! :%s" % e)
                logger.error("DIR : %s" % self.path_out)

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
        # 计数
        total = 0
        for full_in in Traverse.get_file(self.path_in):
            total += 1
            name = full_in.replace("\\", "/").split("/")[-1]
            logger.info("counting : %d\t%s" % (total, name))
        # 开始
        jetzt = 0
        for full_in in Traverse.get_file(self.path_in):
            jetzt += 1
            full_in = full_in.replace("\\", "/")
            # 单文件名
            name = full_in.split("/")[-1]
            # 对root的相对路径
            name_upper_dir = full_in.replace(self.path_in + "/", "")
            # 完整输出路径
            full_out = os.path.join(self.path_out, name_upper_dir).replace("\\", "/")
            state = self.__method_merge(full_in, full_out)
            logger.info("%s\t%d/%d\t%s" % (state, jetzt, total, full_in))
