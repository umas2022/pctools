'''
create: 2022.9.20

对比删除差异
'''

import os
from shutil import copyfile
import shutil
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse


class RemoveDifference():
    def __init__(self, base_path="", del_path="", path_log="",json_set={}) -> None:
        self.base_path = str(base_path).replace("\\", "/")
        self.del_path = str(del_path).replace("\\", "/")
        self.path_log = str(path_log).replace("\\", "/")
        if not json_set == {}:
            try:
                self.base_path = json_set['base_path'].replace("\\", "/")
                self.del_path = json_set['del_path'].replace("\\", "/")
                self.path_log = json_set['path_log'].replace("\\", "/") if "path_log" in json_set else ""
            except Exception as e:
                logger.error("key error: %s" %e)
                return

    def __remove_dir(self, methodPathBasic, methodPathDel):
        '''处理方法：删除文件夹'''
        if os.path.isdir(methodPathBasic):
            return "dir pass"
        else:
            try:
                if (not self.path_log == "") and self.path_log in methodPathDel:
                    return "skip log"
                shutil.rmtree(methodPathDel)
                return "dir delete"
            except Exception as e:
                logger.error("RemoveDifference - remove dir error :%s" % e)
                logger.error("dir : %s" % methodPathDel)
                return "error"

    def __remove_file(self, methodPathBasic, methodPathDel):
        '''处理方法：删除文件'''
        if os.path.isfile(methodPathBasic):
            return "file pass"
        else:
            try:
                if (not self.path_log == "") and self.path_log in methodPathDel:
                    return "skip log"
                os.remove(methodPathDel)
                return "file delete"
            except Exception as e:
                logger.error("RemoveDifference - remove file error :%s" % e)
                logger.error("file : %s" % methodPathDel)
                return "error"

    def run(self):
        '''开始处理'''
        logger.info("remove difference function start ...")
        # 文件夹删除
        logger.write("remove difference - dir")
        total = 0
        for full_del in Traverse().get_dir(self.del_path):
            total += 1
            name = full_del.replace("\\", "/").split("/")[-1]
            logger.info("dir counting : %d\t%s" % (total, name))
        logger.write("total dir : %d\n" % total)
        # 开始
        jetzt = 0
        # 遍历被将要删除的路径
        for full_del in Traverse().get_dir(self.del_path):
            jetzt += 1
            full_del = full_del.replace("\\", "/")
            # 单文件名
            name = full_del.split("/")[-1]
            # 对root的相对路径
            name_upper_dir = full_del.replace(self.del_path + "/", "")
            # 对比基准路径
            full_base = os.path.join(self.base_path, name_upper_dir).replace("\\", "/")
            state = self.__remove_dir(full_base, full_del)
            logger.info("%s\t%d/%d\t%s" % (state, jetzt, total, full_del))

        # 文件删除
        # 计数
        logger.write("remove difference - file")
        total = 0
        for full_del in Traverse().get_file(self.del_path):
            total += 1
            name = full_del.replace("\\", "/").split("/")[-1]
            logger.info("file counting : %d\t%s" % (total, name))
        logger.write("total file : %d\n" % total)
        # 开始
        jetzt = 0
        for full_del in Traverse().get_file(self.del_path):
            jetzt += 1
            full_del = full_del.replace("\\", "/")
            # 单文件名
            name = full_del.split("/")[-1]
            # 对root的相对路径
            name_upper_dir = full_del.replace(self.del_path + "/", "")
            # 完整输出路径
            full_base = os.path.join(self.base_path, name_upper_dir).replace("\\", "/")
            state = self.__remove_file(full_base, full_del)
            logger.info("rm-dif: %s\t%d/%d\t%s" % (state, jetzt, total, full_del))
