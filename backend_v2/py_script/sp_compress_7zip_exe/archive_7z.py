'''
create: 2023.1.26

文件夹批量打包7zip
'''

import os
import sys
import threading
import subprocess
import time
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse


class Archive7z():
    '''文件夹批量打包7zip\n
    必要参数：path_in,path_out, password'''

    def __init__(self, path_in="", path_out="", password="", path_log="", path_7z="", thread_num=1, json_set={}) -> None:
        self.path_in = str(path_in).replace("\\", "/")
        self.path_out = str(path_out).replace("\\", "/")
        self.path_log = str(path_log).replace("\\", "/")
        self.path_7z = str(path_7z).replace("\\", "/")
        logger.raw_logger.set_path(str(path_log).replace("\\", "/"))
        self.password = str(password)
        self.thread_num = int(thread_num)
        if not json_set == {}:
            try:
                self.path_in = json_set['path_in'].replace("\\", "/")
                self.path_out = json_set['path_out'].replace("\\", "/")
                self.path_log = json_set['path_log'].replace("\\", "/") if "path_log" in json_set else ""
                self.path_7z = json_set['path_7z'].replace("\\", "/")
                self.password = json_set['password']
                self.thread_num = int(json_set['thread_num'])
            except Exception as e:
                logger.error("key error: %s" % e)
                return

        # 多线程是否完成
        self.all_done_flag = False
        # 多线程一组内完成的数量
        self.th_ready_num = 0
        # 当前已经完成的数量
        self.jetzt_done = 0
        # 总数
        self.total = 0

    def __7zip_compress(self, methodPathIn, methodPathOut) -> str:
        '''处理方法分类器'''
        # 创建输出目录结构
        state = ""
        try:
            name = methodPathIn.replace("\\", "/").split("/")[-1]
            methodPathOut = methodPathOut + ".7z"

            script_dir = os.path.split(os.path.realpath(__file__))[0]
            script = os.path.join(script_dir, "call_exe.py")
            print(script)
            subprocess.run(['python', script,self.path_7z,methodPathIn,methodPathOut,self.password], creationflags=subprocess.CREATE_NEW_CONSOLE)

            state = "done"
        except Exception as e:
            logger.error("Archive7z ERROR !!! :%s" % e)
            logger.error("dir : %s" % methodPathIn)
            state = "error"

        self.jetzt_done += 1
        self.th_ready_num += 1
        if self.jetzt_done == self.total:
            self.all_done_flag = True
        logger.info("%s\t%d/%d\t%s" % (state, self.jetzt_done, self.total, methodPathIn))

    def run(self):
        '''开始处理'''
        logger.info("7zip compress function start ...")
        logger.write("7zip compress")
        # 计数
        for full_in in Traverse().get_first_dir(self.path_in):
            self.total += 1
            name = full_in.replace("\\", "/").split("/")[-1]
            logger.info("counting : %d\t%s" % (self.total, name))
        logger.write("total : %d\n" % self.total)
        # 开始
        th_count = 0
        for full_in in Traverse().get_first_dir(self.path_in):
            full_in = full_in.replace("\\", "/")
            # 单文件名
            name = full_in.split("/")[-1]
            # 对root的相对路径
            name_upper_dir = full_in.replace(self.path_in + "/", "")
            # 完整输出路径
            full_out = os.path.join(self.path_out, name_upper_dir).replace("\\", "/")

            # 开启新线程
            new_th = threading.Thread(target=self.__7zip_compress, args=[full_in, full_out], daemon=True)
            new_th.start()
            th_count += 1
            if th_count % self.thread_num == 0:
                self.th_ready_num = 0
                # 等待组内全部完成
                while self.th_ready_num < self.thread_num:
                    time.sleep(1)

        # 等待所有任务全部完成
        while not self.all_done_flag:
            time.sleep(1)
