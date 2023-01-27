'''
create: 2022.9.20

图片压缩
'''

import os
from shutil import copyfile
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse


class CopyCheck():
    def __init__(self, path_in, path_out,path_log = "") -> None:
        self.path_in = str(path_in).replace("\\", "/")
        self.path_out = str(path_out).replace("\\", "/")
        self.path_log = str(path_log).replace("\\", "/")
        logger.raw_logger.set_path(str(path_log).replace("\\", "/"))
        self.in_amount = 0
        self.in_size = 0
        self.out_amount = 0
        self.out_size = 0

    def __size_format(self, raw_size):
        if int(raw_size / 1024 / 1024 / 1024) > 0:
            return "%.3f GB" % (raw_size / 1024 / 1024 / 1024)
        elif int(raw_size / 1024 / 1024) > 0:
            return "%.3f MB" % (raw_size / 1024 / 1024)
        elif int(raw_size / 1024) > 0:
            return "%.3f KB" % (raw_size / 1024)
        else:
            return "%d B" % (raw_size)

    def run(self):
        '''开始处理'''
        logger.info("copy check function start ...")
        logger.write("copy check")
        # path_in计数
        for full_in in Traverse().get_file(self.path_in):
            self.in_amount += 1
            self.in_size += os.path.getsize(full_in)
            name = full_in.replace("\\", "/").split("/")[-1]
            logger.info("path_in counting : %d\t%s" % (self.in_amount, name))
        # path_out计数
        for full_out in Traverse().get_file(self.path_out):
            self.out_amount += 1
            self.out_size += os.path.getsize(full_out)
            name = full_out.replace("\\", "/").split("/")[-1]
            logger.info("path_out counting : %d\t%s" % (self.out_amount, name))
        # 结果返回
        logger.info("\n\n====================\n")
        logger.info("path_in amount : %d" % self.in_amount)
        logger.info("path_in size : %s" % self.__size_format(self.in_size))
        logger.info("path_out amount : %d" % self.out_amount)
        logger.info("path_out size : %s" % self.__size_format(self.out_size))

        logger.write("path_in amount : %d" % self.in_amount)
        logger.write("path_in size : %s" % self.__size_format(self.in_size))
        logger.write("path_out amount : %d" % self.out_amount)
        logger.write("path_out size : %s" % self.__size_format(self.out_size))
