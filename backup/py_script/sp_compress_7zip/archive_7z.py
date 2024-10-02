'''
create: 2023.1.26

文件夹批量打包7zip
提供两种打包方法: 1.py7zr, 2.调用已经安装好的7z.exe
'''

import os
import sys
import threading
import subprocess
import time
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse
from utils_tools.string_tools import StringTools
import py7zr  # pip install py7zr


class Archive7z():
    '''文件夹批量打包7zip\n
    必要参数：path_in,path_out, password'''

    def __init__(self, method="", path_in="", path_out="", password="", path_log="", path_7z="", th_total=1, overwrite=False, keyword="", location="", double_cp=False,deep=False, json_set={}) -> None:
        # 多线程是否完成
        self.all_done_flag = True
        # 多线程已经在组内的数量
        self.th_running = 0
        # 当前已经完成的数量
        self.jetzt_done = 0
        # 总数
        self.total = 0

        self.method = str(method)
        self.path_in = str(path_in).replace("\\", "/")
        self.path_out = str(path_out).replace("\\", "/")
        self.path_log = str(path_log).replace("\\", "/")
        logger.set_path(str(path_log).replace("\\", "/"))
        self.path_7z = str(path_7z).replace("\\", "/")
        self.password = str(password)
        self.th_total = int(th_total)
        self.overwrite = bool(overwrite)
        self.keyword = str(keyword)
        self.location = str(location)
        self.double_cp = bool(double_cp)
        self.deep = bool(deep)
        if not json_set == {}:
            try:
                self.method = json_set['method']
                self.path_in = json_set['path_in'].replace("\\", "/")
                self.path_out = json_set['path_out'].replace("\\", "/")
                self.path_log = json_set['path_log'].replace("\\", "/") if "path_log" in json_set else ""
                self.path_log = "" if self.path_log == "." else self.path_log
                logger.set_path(self.path_log)
                self.path_7z = json_set['path_7z'].replace("\\", "/") if "path_7z" in json_set else ""
                self.password = json_set['password']
                self.th_total = int(json_set['th_total'])
                self.overwrite = bool(json_set['overwrite'])
                self.keyword = json_set['keyword'] if "keyword" in json_set else ""
                self.location = json_set['location'] if "location" in json_set else ""
                self.double_cp = bool(json_set['double_cp']) if "double_cp" in json_set else False
                self.deep = bool(json_set['deep']) if "deep" in json_set else False
            except Exception as e:
                logger.error("key error: %s" % e)
                return

    def __check_keyword(self, target) -> bool:
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
                return StringTools().location_match(target, self.keyword, int(self.location))

    def __cp_exe(self, methodPathIn, methodPathOut):
        '''调用7z.exe压缩'''
        try:
            script_dir = os.path.split(os.path.realpath(__file__))[0]
            script = os.path.join(script_dir, "call_exe.py")
            subprocess.run(['python', script, self.path_7z, methodPathIn, methodPathOut, self.password], creationflags=subprocess.CREATE_NEW_CONSOLE)
            # subprocess.run(['python', script, self.path_7z, methodPathIn, methodPathOut, self.password])
            return "compress"
        except Exception as e:
            logger.error("Archive7z - exe compress error !!! :%s" % e)
            logger.error("path_in : %s" % methodPathIn)
            return "error"

    def __cp_py7zr(self, methodPathIn, methodPathOut):
        '''调用py7zr压缩'''
        try:
            name = os.path.split(methodPathIn)[1]
            with py7zr.SevenZipFile(methodPathOut, 'w', password=self.password) as archive:
                archive.writeall(methodPathIn, name)
            return "compress"
        except Exception as e:
            logger.error("Archive7z - py7zr compress error !!! :%s" % e)
            logger.error("path_in : %s" % methodPathIn)
            return "error"

    def __cp_filter(self, methodPathIn, methodPathOut) -> str:
        '''处理方法分类器'''
        self.all_done_flag = False
        # 创建输出目录结构
        name = methodPathIn.split("/")[-1]
        dir_out = os.path.split(methodPathOut)[0]
        if not os.path.exists(dir_out):
            try:
                os.makedirs(dir_out)
            except Exception as e:
                logger.error("Archive7z - makedir error !!! :%s" % e)
                logger.error("dir_out : %s" % dir_out)
        # 开始压缩
        state = ""
        # 检测是否跳过已存在的压缩包
        double_suffix = os.path.splitext(methodPathOut)[1]
        double_path = os.path.splitext(methodPathOut)[0] + "_cp2"
        double_path = double_path + double_suffix
        if (not self.overwrite) and os.path.isfile(methodPathOut):
            state = "exist"
        elif (not self.overwrite) and os.path.isfile(double_path):
            state = "exist"
        else:
            # 压缩方法分类
            cp_method = ""
            if self.method == "py7zr":
                cp_method = self.__cp_py7zr
            elif self.method == "exe":
                cp_method = self.__cp_exe
            else:
                logger.error("unexpected method : %s" % self.method)
                return
            # 调用压缩函数
            state = cp_method(methodPathIn, methodPathOut)
            if self.double_cp:
                logger.info("%s\t%d/%d\t%s" % ("first_cp done : ", self.jetzt_done+1, self.total, methodPathIn))
                double_suffix = os.path.splitext(methodPathOut)[1]
                double_path = os.path.splitext(methodPathOut)[0] + "_cp2"
                double_path = double_path + double_suffix
                state = cp_method(methodPathOut,double_path)
                if state == "compress":
                    os.remove(methodPathOut)
                    state = "double_cp done : "


        self.jetzt_done += 1
        self.th_running -= 1
        if self.jetzt_done == self.total:
            self.all_done_flag = True
        logger.info("%s\t%d/%d\t%s" % (state, self.jetzt_done, self.total, methodPathIn))

    def run(self):
        '''开始处理'''
        logger.info("7zip compress function start ...")
        logger.write("7zip compress")

        target_list = []
        if self.deep:
            target_list = Traverse().get_dir
        else:
            target_list = Traverse().get_first_dir
        # 计数
        for full_in in target_list(self.path_in):
            name = full_in.replace("\\", "/").split("/")[-1]
            if self.__check_keyword(name):
                self.total += 1
                logger.info("counting : %d\t%s" % (self.total, name))
        logger.write("total : %d\n" % self.total)
        # 开始
        for full_in in target_list(self.path_in):
            full_in = full_in.replace("\\", "/")
            # 单文件名
            name = full_in.split("/")[-1]
            if self.__check_keyword(name):
                # 对root的相对路径
                name_upper_dir = full_in.replace(self.path_in + "/", "")
                # 完整输出路径
                full_out = os.path.join(self.path_out, name_upper_dir).replace("\\", "/")
                full_out += ".7z"
                # 开启新线程
                new_th = threading.Thread(target=self.__cp_filter, args=[full_in, full_out], daemon=True)
                new_th.start()
                self.th_running += 1
                # 等待组内有任务完成
                while self.th_running == self.th_total:
                    time.sleep(1)

        # 等待所有任务全部完成
        while not self.all_done_flag:
            time.sleep(1)

