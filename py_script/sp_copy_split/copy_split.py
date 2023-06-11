'''
create: 2023.4.19
拷贝拆分,目标只有输入第一级目录下的文件,没有deep参数
'''

import os
from shutil import copyfile
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse
from utils_tools.traverse_copy import TVcopy


class CopySplit(TVcopy):
    def __init__(self, json_set={}) -> None:
        try:
            # *输入路径
            self.path_in = os.path.normpath(json_set['path_in'])
            # *输出路径
            self.path_out = os.path.normpath(json_set['path_out'])
            # 日志路径(默认无)
            self.path_log = os.path.normpath(json_set['path_log']) if "path_log" in json_set else ""
            logger.set_path(str(self.path_log).replace("\\", "/"))
            # 程序控制:是否计数(默认True)
            self.if_count = bool(json_set['if_count']) if "if_count" in json_set else True
            TVcopy.__init__(self,self.path_in,self.path_out,self.path_log,self.if_count)


            # *单包容量
            self.single_cap = int(json_set['single_cap'])
            # 命名方法(默认序号命名)
            self.name_func = json_set['name_func'] if "name_func" in json_set else "by_num"
        except Exception as e:
            logger.error("key error: %s" % e)
            return

    def __path_join(self, in_path_out, in_dir):
        '''拼接输出路径,将分包文件夹添加到路径中'''
        root_dir = os.path.split(in_path_out)[0]
        root_name = os.path.split(in_path_out)[1]
        return os.path.normpath(os.path.join(root_dir, in_dir, root_name))

    def func_handle(self, methodPathIn, methodPathOut, jetzt):
        '''处理方法：拷贝拆分'''
        root_dir = os.path.split(methodPathOut)[0]
        root_name = os.path.split(methodPathOut)[1]

        # 创建当前文件所属的包目录
        pack_num = (jetzt - 1) // self.single_cap +1
        pack_num = str(pack_num).zfill(3)
        pack_path = os.path.normpath(os.path.join(root_dir, str(pack_num)))
        if not os.path.exists(pack_path):
            try:
                os.makedirs(pack_path)
            except Exception as e:
                logger.error("make dir error :%s" % e)
                logger.error("dir : %s" % pack_path)

        # 复制文件到包
        sp_out = self.__path_join(methodPathOut, str(pack_num))

        if os.path.isfile(sp_out):
            return "pass"
        else:
            try:
                copyfile(methodPathIn, sp_out)
                return "copy"
            except Exception as e:
                logger.error("copy error :%s" % e)
                logger.error("file : %s" % methodPathIn)
                return "error"

    def run(self):
        '''开始处理'''
        logger.info("copy split function start ...")
        logger.write("copy split")
        self.find_all(Traverse().get_first_file,self.func_handle)

