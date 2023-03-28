'''
create: 2022.9.20

图片压缩
'''

import os
from shutil import copyfile
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse


class SearchSuffix():
    def __init__(self, json_set={}) -> None:
        if not json_set == {}:
            try:
                self.path_in = json_set['path_in'].replace("\\", "/")
                self.path_log = json_set['path_log'].replace("\\", "/") if "path_log" in json_set else ""
                logger.raw_logger.set_path(os.path.normpath(str(self.path_log)))
            except Exception as e:
                logger.error("key error: %s" % e)
                return

        self.suffix_list = []

    def __suffix_filter(self, methodPathIn):
        '''处理方法：搜索所有后缀名'''
        name = os.path.split(methodPathIn)[-1]
        suffix = str(name).split(".")[-1]
        if not suffix in self.suffix_list:
            self.suffix_list.append(suffix)
        return suffix

    def run(self):
        '''开始处理'''
        logger.info("search suffix function start ...")
        logger.write("search suffix")
        jetzt = 0
        for full_in in Traverse().get_file(self.path_in):
            jetzt += 1
            full_in = os.path.normpath(full_in)
            state = self.__suffix_filter(full_in)
            logger.info("%s\t%d\t%s" % (state, jetzt, full_in))
        logger.info("all suffix: %s" % str(self.suffix_list))
