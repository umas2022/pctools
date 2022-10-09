'''
create: 2022.9.20

图片压缩
'''

import os
from shutil import copyfile

from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse


class RenameBasic():
    def __init__(self, path_in, use_func, add_in="", path_log="") -> None:
        '''
        path_in: 输入路径
        use_func: 重命名方法
        add_in: 附加输入参数
        path_log: 日志路径(置空不使用日志)
        '''
        self.path_in = str(path_in).replace("\\", "/")
        logger.raw_logger.set_path(str(path_log).replace("\\", "/"))
        self.use_func = use_func
        self.add_in = add_in

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

    def __filter(self, methodPathIn: str, jetzt: int):
        '''处理方法分类器'''
        if not os.path.isfile(methodPathIn):
            logger.error("RenameBasic: no such file - %s" % methodPathIn)
            return "error"
        # 添加前缀
        if self.use_func == "add_prefix":
            state, methodPathOut = self.__method_add_prefix(methodPathIn, jetzt)
        # 删除前缀
        elif self.use_func == "del_prefix":
            state, methodPathOut = self.__method_del_prefix(methodPathIn, jetzt)
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
            # 调用filter
            state = self.__filter(full_in, jetzt)
            logger.info("%s\t%d/%d\t%s" % (state, jetzt, total, full_in))
