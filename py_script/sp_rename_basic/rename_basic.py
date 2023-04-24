'''
create: 2022.9.20

图片压缩
'''

import os
from shutil import copyfile

from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse
from utils_path.upath import *


class RenameBasic():
    def __init__(self, path_in="", use_func="", target="file", add_in="", add_in_2="", path_log="",deep=False, json_set={}) -> None:
        '''
        path_in: 输入路径
        use_func: 重命名方法
        add_in: 附加输入参数
        path_log: 日志路径(置空不使用日志)
        '''
        self.path_in = str(path_in).replace("\\", "/")
        logger.set_path(str(path_log).replace("\\", "/"))
        self.use_func = use_func
        self.target = target
        self.add_in = add_in
        self.add_in_2 = add_in_2
        self.deep = deep
        if not json_set == {}:
            try:
                self.path_in = json_set['path_in'].replace("\\", "/")
                self.path_log = json_set['path_log'].replace("\\", "/") if "path_log" in json_set else ""
                logger.set_path(self.path_log)
                self.use_func = json_set['use_func']
                self.target = json_set['target'] if "target" in json_set else "file"
                self.add_in = json_set['add_in']if "add_in" in json_set else ""
                self.add_in_2 = json_set['add_in_2']if "add_in_2" in json_set else ""
                self.deep = json_set['deep']if "deep" in json_set else False
            except Exception as e:
                logger.error("key error: %s" % e)
                return

    def __method_add_prefix(self, methodPathIn: str, jetzt: int):
        '''处理方法: 添加前缀'''
        methodPathIn = methodPathIn.replace("\\", "/")
        dir, name = os.path.split(methodPathIn)
        name_new = self.add_in + name
        methodPathOut = os.path.join(dir, name_new).replace("\\", "/")
        return "add_prefix", methodPathOut

    def __method_del_prefix(self, methodPathIn: str, jetzt: int):
        '''处理方法: 删除前缀'''
        state = "del_prefix"
        methodPathIn = methodPathIn.replace("\\", "/")
        dir, name = os.path.split(methodPathIn)
        name_list = name.split(self.add_in)
        if name_list[0] == "":
            del (name_list[0])
        else:
            state = "pass"
        name_new = self.add_in.join(name_list)
        methodPathOut = os.path.join(dir, name_new).replace("\\", "/")
        return state, methodPathOut

    def __method_replace_key(self, methodPathIn: str, jetzt: int):
        '''处理方法: 关键字替换'''
        state = "replace_key"
        methodPathIn = methodPathIn.replace("\\", "/")
        dir, name = os.path.split(methodPathIn)
        if self.add_in in name:
            name_list = name.split(self.add_in)
            name_new = self.add_in_2.join(name_list)
            methodPathOut = os.path.join(dir, name_new).replace("\\", "/")
        else:
            state = "pass"
            methodPathOut = methodPathIn
        return state, methodPathOut

    def __method_num_array(self,methodPathIn: str, jetzt: int):
        '''处理方法: 三位数字序号命名'''
        state = "num_array"
        methodPathIn = methodPathIn.replace("\\", "/")
        dir, name = os.path.split(methodPathIn)
        fileFormat = ""
        if self.target == "file":
            fileFormat = name.split(".")[-1]
        name_new = str(jetzt+int(self.add_in_2)-1).zfill(int(self.add_in))+"."+fileFormat
        methodPathOut = os.path.join(dir, name_new).replace("\\", "/")
        return state, methodPathOut

    def __filter(self, methodPathIn: str, jetzt: int):
        '''处理方法分类器'''
        if not os.path.isfile(methodPathIn):
            if not os.path.isdir(methodPathIn):
                logger.error("RenameBasic: no such file - %s" % methodPathIn)
                return "error"
        # 添加前缀
        if self.use_func == "add_prefix":
            state, methodPathOut = self.__method_add_prefix(methodPathIn, jetzt)
        # 删除前缀
        elif self.use_func == "del_prefix":
            state, methodPathOut = self.__method_del_prefix(methodPathIn, jetzt)
        # 关键字替换
        elif self.use_func == "replace_key":
            state, methodPathOut = self.__method_replace_key(methodPathIn, jetzt)
        # 序号命名
        elif self.use_func == "num_array":
            state, methodPathOut = self.__method_num_array(methodPathIn, jetzt)
        else:
            logger.error("暂时还没写其他的方法！")
        try:
            os.rename(methodPathIn, methodPathOut)
            return state
        except Exception as e:
            logger.error("RenameBasic: rename failed - %s" % e)
            return "error"

    def run(self):
        '''开始处理'''
        logger.info("rename function start ...")
        logger.write("rename %s" % self.use_func)
        # 分类
        total = 0
        tarverse_func = ""
        if self.target == "dir":
            if self.deep:
                tarverse_func = Traverse().get_dir
            else:
                tarverse_func = Traverse().get_first_dir
        elif self.target == "file":
            if self.deep:
                tarverse_func = Traverse().get_file
            else:
                tarverse_func = Traverse().get_first_file
        else:
            logger.error("remove_keyword : unexpected target - %s" % self.target)
            return
        # 计数
        for full_in in tarverse_func(self.path_in):
            total += 1
            name = full_in.replace("\\", "/").split("/")[-1]
            logger.info("counting : %d\t%s" % (total, name))
        logger.write("total : %d\n" % total)
        # 开始
        jetzt = 0
        for full_in in tarverse_func(self.path_in):
            jetzt += 1
            full_in = full_in.replace("\\", "/")
            # 调用filter
            state = self.__filter(full_in, jetzt)
            logger.info("%s\t%d/%d\t%s" % (state, jetzt, total, full_in))
