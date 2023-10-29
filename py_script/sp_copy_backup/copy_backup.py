'''
create: 2022.9.20

文件复制,支持关键字筛选
'''

import os
from shutil import copyfile
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse
from utils_tools.traverse_copy import TVcopy
from utils_tools.string_tools import StringTools

class CopyBackup(TVcopy):
    def __init__(self,json_set = {}) -> None:
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
            # 程序控制:是否检测重名文件的大小
            self.check_size = bool(json_set['check_size']) if "check_size" in json_set else False
            # 内部：重名文件大小模糊系数（除以系数取整，取1024即检测精度到KB为止）
            self.__fuzzy = 1024

            # 关键词匹配
            self.keyword = json_set['keyword'] if "keyword" in json_set else ""
            # 关键词位置
            self.location = json_set['location'] if "location" in json_set else ""
            
        except Exception as e:
            logger.error("CopyBackup - key error: %s" % e)
            return

            
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


    def func_handle(self, methodPathIn, methodPathOut,jetzt):
        '''处理方法：完全备份'''

        state = "copy"

        # 创建输出目录结构
        dir_out = os.path.split(methodPathOut)[0]
        if not os.path.exists(dir_out):
            try:
                os.makedirs(dir_out)
            except Exception as e:
                logger.error("CopyBackup - make dir error !!! :%s" % e)
                logger.error("path : %s" % dir_out)

        # 存在同名文件
        if os.path.isfile(methodPathOut):
            # 检测两文件大小
            if self.check_size:
                size_in = int(os.path.getsize(methodPathIn) / self.__fuzzy)
                size_out = int(os.path.getsize(methodPathOut) / self.__fuzzy)
                if size_in == size_out:
                    return "exist"
                else:
                    state = "cover"
            else:
                return "exist"
        # 拷贝
        try:
            name = os.path.split(methodPathOut)[-1]
            if self.__check_keyword(name):
                copyfile(methodPathIn, methodPathOut)
                return state
            else:
                return "pass"
        except Exception as e:
            logger.error("CopyBackup - copy error !!! :%s" % e)
            logger.error("path : %s" % methodPathIn)
            return "error"

    def run(self):
        '''开始处理'''
        logger.info("copy backup function start ...")
        logger.write("copy backup")
        self.find_all(Traverse().get_file,self.func_handle)


