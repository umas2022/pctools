'''
create: 2023.2.12

wsa文件拷贝

2023.6 : 放弃win11,此脚本不再更新
'''

import os
import time
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse
import subprocess
from utils_tools.string_tools import StringTools

class CopyWsa():
    def __init__(self,path_adb="",adb_port="", path_in="", path_out="",path_log = "",keyword="",location="",json_set = {}) -> None:
        self.path_adb = str(path_adb).replace("\\", "/")
        self.adb_port = str(adb_port)
        self.path_in = str(path_in).replace("\\", "/")
        self.path_out = str(path_out).replace("\\", "/")
        logger.set_path(str(path_log).replace("\\", "/"))
        self.keyword = str(keyword)
        self.location = str(location)
        if not json_set == {}:
            try:
                self.path_adb = json_set['path_adb'].replace("\\", "/")
                self.adb_port = json_set['adb_port']
                self.path_in = json_set['path_in'].replace("\\", "/")
                self.path_out = json_set['path_out'].replace("\\", "/")
                self.path_log = json_set['path_log'] if "path_log" in json_set else ""
                logger.set_path(self.path_log)
                self.keyword = json_set['keyword'] if "keyword" in json_set else ""
                self.location = json_set['location'] if "location" in json_set else ""
            except Exception as e:
                logger.error("key error: %s" %e)
                return
            


    def __adb_push(self,methodPathIn, methodPathOut):
        '''调用adb传送文件'''
        subprocess.run([self.path_adb,"-s", self.adb_port,"push","--sync",methodPathIn,methodPathOut])          

    def __check_keyword(self,target) -> bool:
        '''匹配关键字'''
        if self.keyword == "":
            return True
        else:
            # 不指定关键字位置
            if self.location == "":
                if self.keyword in target:
                    return True
                else:
                    return False
            # 指定关键字位置
            else:
                return StringTools().location_match(target,self.keyword,int(self.location))



    def __copy_filter(self, methodPathIn, methodPathOut):
        '''处理方法：完全备份'''
        name = os.path.split(methodPathIn)[1]
        try:
            if self.__check_keyword(name):
                self.__adb_push(methodPathIn, methodPathOut)
                return "copy"
            else:
                return "pass"
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


        # adb连接
        subprocess.run([self.path_adb,"connect", self.adb_port])

        # 开始复制
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
