'''
create: 2023.1.26

文件夹批量打包7zip
'''

import os
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse
import py7zr # pip install py7zr

class Archive7z():
    '''文件夹批量打包7zip\n
    必要参数：path_in,path_out, password'''

    def __init__(self, path_in="",path_out="", password="", path_log="", json_set={}) -> None:
        self.path_in = str(path_in).replace("\\", "/")
        self.path_out = str(path_out).replace("\\", "/")
        self.password = str(password)
        logger.raw_logger.set_path(str(path_log).replace("\\", "/"))
        if not json_set == {}:
            try:
                self.path_in = json_set['path_in'].replace("\\", "/")
                self.path_out = json_set['path_out'].replace("\\", "/")
                self.password = json_set['password']
                self.path_log = json_set['path_log'].replace("\\", "/") if "path_log" in json_set else ""
            except Exception as e:
                logger.error("key error: %s" % e)
                return


    def __7zip_compress(self, methodPathIn, methodPathOut) -> str:
        '''处理方法分类器'''
        # 创建输出目录结构
        try:
            name = methodPathIn.replace("\\", "/").split("/")[-1]
            methodPathOut = methodPathOut+".7z"
            with py7zr.SevenZipFile(methodPathOut,'w',password=self.password) as archive:
                archive.writeall(methodPathIn,name)
            return "compress"
        except Exception as e:
            logger.error("Archive7z ERROR !!! :%s" % e)
            logger.error("dir : %s" % methodPathIn)
            return "error"

    def run(self):
        '''开始处理'''
        logger.info("7zip compress function start ...")
        logger.write("7zip compress")
        # 计数
        total = 0
        for full_in in Traverse().get_first_dir(self.path_in):
            total += 1
            name = full_in.replace("\\", "/").split("/")[-1]
            logger.info("counting : %d\t%s" % (total, name))
        logger.write("total : %d\n" % total)
        # 开始
        jetzt = 0
        for full_in in Traverse().get_first_dir(self.path_in):
            full_in = full_in.replace("\\", "/")
            # 单文件名
            name = full_in.split("/")[-1]
            # 对root的相对路径
            name_upper_dir = full_in.replace(self.path_in + "/", "")
            # 完整输出路径
            full_out = os.path.join(self.path_out, name_upper_dir).replace("\\", "/")
            state = self.__7zip_compress(full_in, full_out)
            if state:
                jetzt += 1
                logger.info("%s\t%d/%d\t%s" % (state, jetzt, total, full_in))
