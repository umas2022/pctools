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

            # 关键词匹配
            self.keyword = json_set['keyword'] if "keyword" in json_set else ""
            # 关键词位置
            self.location = json_set['location'] if "location" in json_set else ""
            
        except Exception as e:
            logger.error("key error: %s" % e)
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

        # 创建输出目录结构
        dir_out = os.path.split(methodPathOut)[0]
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
                name = os.path.split(methodPathOut)[-1]
                if self.__check_keyword(name):
                    copyfile(methodPathIn, methodPathOut)
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
        self.find_all(Traverse().get_file,self.func_handle)

        # # 计数
        # total = 0
        # for full_in in Traverse().get_file(self.path_in):
        #     total += 1
        #     name = full_in.replace("\\", "/").split("/")[-1]
        #     logger.info("counting : %d\t%s" % (total, name))
        # logger.write("total : %d\n" % total)
        # # 开始
        # jetzt = 0
        # for full_in in Traverse().get_file(self.path_in):
        #     jetzt += 1
        #     full_in = full_in.replace("\\", "/")
        #     # 单文件名
        #     name = full_in.split("/")[-1]
        #     # 对root的相对路径
        #     name_upper_dir = full_in.replace(self.path_in + "/", "")
        #     # 完整输出路径
        #     full_out = os.path.join(self.path_out, name_upper_dir).replace("\\", "/")
        #     state = self.__copy_filter(full_in, full_out)
        #     logger.info("%s\t%d/%d\t%s" % (state, jetzt, total, full_in))
