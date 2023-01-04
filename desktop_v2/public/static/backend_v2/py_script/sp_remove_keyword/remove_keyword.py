'''
create: 2022.9.27

删除包含指定关键词的文件
'''

import os
from shutil import copyfile
import shutil
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse


class RemoveKeyword():
    '''删除包含指定关键字的文件/文件夹'''

    def __init__(self, path_in="", keyword="", keyword_and="", path_log="", target="file", cut_mode=False, cut_path="", json_set={}) -> None:
        self.path_in = str(path_in).replace("\\", "/")
        # 如果日志路径包含在被删除目录中,将被直接跳过不作删除
        self.path_log = str(path_log).replace("\\", "/")
        # 主要字段,置空匹配所有文件
        self.keyword = keyword
        # 次要字段,与主要字段同时存在时判断成立，置空不使用次要字段
        self.keyword_and = keyword_and
        # 删除目标,取值:["file","dir"]对应文件或文件夹
        self.target = target
        # 试错模式,启用后目标将被移动到试错目录,而不是直接删除
        self.cut_mode = cut_mode
        # 试错目录,置空不使用试错模式
        self.cut_path = cut_path

        if not json_set == {}:
            try:
                self.path_in = json_set['path_in'].replace("\\", "/")
                self.path_log = json_set['path_log'].replace("\\", "/") if "path_log" in json_set else ""
                self.keyword = json_set['keyword']
                self.keyword_and = json_set['keyword_and']
                self.target = json_set['target'] if "target" in json_set else "file"
                self.cut_mode = json_set['cut_mode'] if "cut_mode" in json_set else False
                self.cut_path = json_set['cut_path'].replace("\\", "/") if "cut_path" in json_set else ""
            except Exception as e:
                logger.error("key error: %s" % e)
                return

    def __remove_filter(self, methodPathIn):
        '''处理方法：删除关键词'''
        name = methodPathIn.split("/")[-1]
        if self.keyword_and in name:
            if self.keyword in name:
                # 日志路径,跳过
                if (not self.path_log == "") and self.path_log in methodPathIn:
                    return "skip log"
                # 检测到目标,直接删除
                if not self.cut_mode or self.cut_path == "":
                    try:
                        if self.target == "dir":
                            shutil.rmtree(methodPathIn)
                        else:
                            os.remove(methodPathIn)
                        return "remove"
                    except Exception as e:
                        logger.error("RemoveKeyword - remove error : %s" % e)
                        logger.error("file : %s" % methodPathIn)
                        return "error"
                # 检测到目标,移动到试错目录
                else:
                    # 创建输出目录结构
                    name_upper_dir = methodPathIn.replace(self.path_in + "/", "")
                    methodPathOut = os.path.join(self.cut_path, name_upper_dir).replace("\\", "/")
                    name = methodPathIn.split("/")[-1]
                    dir_out = methodPathOut.replace("/" + name, "")
                    if not os.path.exists(dir_out):
                        try:
                            os.makedirs(dir_out)
                        except Exception as e:
                            logger.error("RemoveKeyword - make dir error :%s" % e)
                            logger.error("file : %s" % dir_out)
                    try:
                        shutil.move(methodPathIn, methodPathOut)
                        return "move"
                    except Exception as e:
                        logger.error("RemoveKeyword - remove error : %s" % e)
                        logger.error("file : %s" % methodPathIn)
                        return "error"
            else:
                return "pass"

    def run(self):
        '''开始处理'''
        logger.info("remove keyword function start ...")
        logger.write("remove keyword")
        # 分类
        total = 0
        tarverse_func = ""
        if self.target == "dir":
            tarverse_func = Traverse().get_dir
        elif self.target == "file":
            tarverse_func = Traverse().get_file
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
        del_count = 0
        for full_in in tarverse_func(self.path_in):
            jetzt += 1
            full_in = full_in.replace("\\", "/")
            state = self.__remove_filter(full_in)
            logger.info("%s\t%d/%d\t%s" % (state, jetzt, total, full_in))
            if state == "remove" or state == "move":
                del_count += 1
        logger.info("total: %d" % total)
        logger.info("delete: %d" % del_count)
