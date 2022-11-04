'''
create: 2022.9.20

图片压缩
'''

import os
from shutil import copyfile
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse


class CopyBackup():
    def __init__(self, path_in="", path_out="",path_log = "",json_set = {}) -> None:
        self.path_in = str(path_in).replace("\\", "/")
        self.path_out = str(path_out).replace("\\", "/")
        logger.raw_logger.set_path(str(path_log).replace("\\", "/"))
        if not json_set == {}:
            try:
                self.path_in = json_set['path_in'].replace("\\", "/")
                self.path_out = json_set['path_out'].replace("\\", "/")
                self.path_log = json_set['path_log'] if "path_log" in json_set else ""
            except Exception as e:
                logger.error("key error: %s" %e)
                return

    def __copy_filter(self, methodPathIn, methodPathOut):
        '''处理方法：完全备份'''

        # 创建输出目录结构
        name = methodPathIn.split("/")[-1]
        dir_out = methodPathOut.replace("/" + name, "")
        if not os.path.exists(dir_out):
            try:
                os.makedirs(dir_out)
            except Exception as e:
                logger.error("sp-ImgCut - MAKEDIR ERROR !!! :%s" % e)
                logger.error("file : %s" % dir_out)

        if os.path.isfile(methodPathOut):
            return "pass"
        else:
            try:
                copyfile(methodPathIn, methodPathOut)
                return "copy"
            except Exception as e:
                logger.error("CopyBackup - COPY ERROR !!! :%s" % e)
                logger.error("file : %s" % methodPathIn)
                return "error"

    def run(self):
        '''开始处理'''
        logger.info("copy backup function start ...")
        logger.write("copy backup")
        # 计数
        total = 0
        for full_in in Traverse().get_file(self.path_in):
            total += 1
            name = full_in.replace("\\", "/").split("/")[-1]
            logger.info("counting : %d\t%s" % (total, name))
        logger.write("total : %d\n" % total)
        # 开始
        jetzt = 0
        for full_in in Traverse().get_file(self.path_in):
            jetzt += 1
            full_in = full_in.replace("\\", "/")
            # 单文件名
            name = full_in.split("/")[-1]
            # 对root的相对路径
            name_upper_dir = full_in.replace(self.path_in + "/", "")
            # 完整输出路径
            full_out = os.path.join(self.path_out, name_upper_dir).replace("\\", "/")
            state = self.__copy_filter(full_in, full_out)
            logger.info("%s\t%d/%d\t%s" % (state, jetzt, total, full_in))
