'''
sp_copy方法专用遍历类,调用traverse.py,
增加了输入输出路径和统计信息
'''

import os
from utils_tools.traverse import Traverse
from utils_logger.log import logger_re as logger

class TVcopy():
    def __init__(self,path_in,path_out,path_log,if_count) -> None:
        # 输入路径
        self.path_in = path_in
        # 输出路径
        self.path_out = path_out
        # 日志路径
        self.path_log = path_log
        # 是否计数
        self.if_count = if_count


    def find_all(self,func_tv,func_hd)->None:
        '''
        func_tv: traverse.py中的遍历方法,如Traverse().get_first_file \n
        func_hd: 处理方法
        '''

        # 计数
        total = 0
        if self.if_count:
            for full_in in func_tv(self.path_in):
                total += 1
                name = os.path.split(os.path.normpath(full_in))[-1]
                logger.info("counting : %d\t%s" % (total, name))
            logger.write("total : %d\n" % total)
        else:
            logger.info("skip count ...")

        # 开始
        jetzt = 0
        for full_in in func_tv(self.path_in):
            jetzt += 1
            full_in = os.path.normpath(full_in)
            # 拼接完整输出路径
            name = os.path.split(full_in)[-1]
            name_upper_dir = os.path.relpath(full_in, self.path_in)
            full_out = os.path.normpath(os.path.join(self.path_out, name_upper_dir))
            # 返回状态
            state = func_hd(full_in, full_out, jetzt)
            logger.info("%s\t%d/%d\t%s" % (state, jetzt, total, full_in))
