'''
create: 2022.9.27

删除包含指定关键词的文件
'''

import os
from shutil import copyfile
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse


class RemoveKeyword():
    def __init__(self, path_in, keyword) -> None:
        self.path_in = str(path_in).replace("\\", "/")
        self.keyword = keyword

    def __remove_filter(self, methodPathIn):
        '''处理方法：删除关键词'''
        name = methodPathIn.split("/")[-1]
        if self.keyword in name:
            try:
                os.remove(methodPathIn)
                return "remove"
            except Exception as e:
                logger.error("RemoveKeyword - remove error : %s" % e)
                logger.error("file : %s" % methodPathIn)
                return "error"
        else:
            return "pass"


    def run(self):
        '''开始处理'''
        logger.info("remove keyword function start ...")
        # 计数
        total = 0
        for full_in in Traverse().get_file(self.path_in):
            total += 1
            name = full_in.replace("\\", "/").split("/")[-1]
            logger.info("counting : %d\t%s" % (total, name))
        # 开始
        jetzt = 0
        for full_in in Traverse().get_file(self.path_in):
            jetzt += 1
            full_in = full_in.replace("\\", "/")
            state = self.__remove_filter(full_in)
            logger.info("%s\t%d/%d\t%s" % (state, jetzt, total, full_in))
