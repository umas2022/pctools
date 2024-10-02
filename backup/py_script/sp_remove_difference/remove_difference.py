'''
create: 2022.9.20

对比删除差异

- 以base_path为基准, 删除del_path中多出的文件, 用于备份后同步删除

'''

import os
from shutil import copyfile
import shutil
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse


class RemoveDifference():
    def __init__(self,json_set={}) -> None:
        # *基准路径
        self.base_path = os.path.normpath(json_set['base_path'])
        # *待删路径
        self.del_path = os.path.normpath(json_set['del_path'])
        # 日志路径(默认无)
        self.path_log = os.path.normpath(json_set['path_log']) if "path_log" in json_set else ""
        logger.set_path(str(self.path_log).replace("\\", "/"))
        # 程序控制:是否计数(默认True)
        self.if_count = bool(json_set['if_count']) if "if_count" in json_set else True


    def __remove_dir(self, methodPathBasic, methodPathDel):
        '''处理方法：删除文件夹'''
        if os.path.isdir(methodPathBasic):
            return "dir pass"
        else:
            try:
                # 跳过日志路径
                if (not self.path_log == "") and self.path_log in methodPathDel:
                    return "skip log"
                # 删除文件夹
                shutil.rmtree(methodPathDel)
                return "dir delete"
            except Exception as e:
                logger.error("RemoveDifference - remove dir error :%s" % e)
                logger.error("path : %s" % methodPathDel)
                return "error"

    def __remove_file(self, methodPathBasic, methodPathDel):
        '''处理方法：删除文件'''
        if os.path.isfile(methodPathBasic):
            return "file pass"
        else:
            try:
                # 跳过日志
                if (not self.path_log == "") and self.path_log in methodPathDel:
                    return "skip log"
                # 删除单个文件
                os.remove(methodPathDel)
                return "file delete"
            except Exception as e:
                logger.error("RemoveDifference - remove file error :%s" % e)
                logger.error("path : %s" % methodPathDel)
                return "error"

    def run(self):
        '''开始处理'''
        logger.info("remove difference function start ...")

        # 文件夹计数
        total = 0
        if self.if_count:
            logger.write("remove difference - dir, counting ...\n")
            for full_del in Traverse().get_dir(self.del_path):
                total += 1
                name = full_del.replace("\\", "/").split("/")[-1]
                logger.info("dir counting : %d\t%s" % (total, name))
            logger.write("total dir : %d\t , deleting ...\n" % total)

        # 文件夹删除
        jetzt = 0
        # 遍历被将要删除的路径
        for full_del in Traverse().get_dir(self.del_path):
            jetzt += 1
            full_del = os.path.normpath(full_del) 
            # 单文件名
            name = full_del.split("/")[-1]
            # 对root的相对路径
            name_upper_dir = os.path.relpath(full_del,self.del_path)
            # 对比基准路径
            full_base = os.path.normpath(os.path.join(self.base_path, name_upper_dir)) 
            state = self.__remove_dir(full_base, full_del)
            logger.info("%s\t%d/%d\t%s" % (state, jetzt, total, full_del))

        # 文件计数
        total = 0
        if self.if_count:
            logger.write("remove difference - file, counting ...\n")
            for full_del in Traverse().get_file(self.del_path):
                total += 1
                name = full_del.replace("\\", "/").split("/")[-1]
                logger.info("file counting : %d\t%s" % (total, name))
            logger.write("total file : %d\t , deleting ...\n" % total)
        
        # 文件删除
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
