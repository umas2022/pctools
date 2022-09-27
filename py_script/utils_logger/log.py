'''
create: 2022.1.1

log控制，经过一次在封装，terminal模式输出可被捕获
from general_basic.log import logger_re as logger
'''


import logging
import time
import os


class logRaw:
    '''原版logger，只在LogRepack中实例化一次，多次实例化会导致重复添加handler，输出重复'''

    def __init__(self, log_path='', set_level="debug"):
        self.path = log_path
        self.file = ""
        self.logger = logging.getLogger('test')

        # logger输出级别
        if set_level == "debug":
            self.logger.setLevel(level=logging.DEBUG)
        else:
            print("其他的还没写啊")

        # 文件输出
        self.set_log_file()

        # 控制台输出
        formatter_console = logging.Formatter(
            '%(asctime)s - %(levelname)s: %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter_console)
        self.logger.addHandler(stream_handler)

    def set_log_file(self):
        '''设置输出log到文件'''
        if self.path != "":
            if not os.path.exists(self.path):
                os.makedirs(self.path)
            time_prefix = time.strftime("%Y-%m-%d_%H.%M", time.localtime())
            self.file = os.path.join(self.path, time_prefix + '.log')

            formatter_file = logging.Formatter(
                '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
            file_handler = logging.FileHandler(self.file, encoding='utf-8')
            file_handler.setLevel(level=logging.WARNING)  # WARNING #INFO
            file_handler.setFormatter(formatter_file)
            self.logger.addHandler(file_handler)

    def set_path(self, path):
        '''重设路径'''
        self.path = path
        self.set_log_file()

    def get_logger(self):
        '''获取logger'''
        return self.logger


class LogRepack:
    '''
    为满足直接调用和前端调用的不同需求，对输出函数进行再封装
    frontend模式用于前端请求，内部为print函数，可以截取标准输出发送至前端
    terminal模式输出原版logger到控制台

    logger = LogRepack("frontend")
    logger.set_mode("terminal")
    '''

    def __init__(self, log_path='', mode_input="terminal") -> None:
        '''self.mode = ["terminal","frontend"]'''
        self.mode = mode_input
        self.raw_logger = logRaw(log_path=log_path)
        self.logger = self.raw_logger.get_logger()

    def get_raw(self):
        '''获取原始logger'''
        return self.raw_logger

    def set_mode(self, mode):
        '''重设模式：两种模式["terminal","frontend"]'''
        self.mode = mode

    def set_path(self, path):
        '''重设log路径，设置后启用文件写入'''
        if not path == "":
            self.raw_logger.set_path(path)

    def write(self, inputstr: any):
        '''直接写入log文件，输入值被str()函数包裹，未指定log文件时print错误并跳过'''
        if self.raw_logger.file == "":
            print("\nlogger.write exit: no log file specified\n")
            return
        with open(self.raw_logger.file, "a") as log_file:
            log_file.write(str(inputstr) + "\n")

    def debug(self, inputstr):
        if self.mode == "terminal":
            self.logger.debug(inputstr)
        elif self.mode == "frontend":
            print("debug : " + inputstr)

    def info(self, inputstr):
        if self.mode == "terminal":
            self.logger.info(inputstr)
        elif self.mode == "frontend":
            print("info : " + inputstr)

    def warning(self, inputstr):
        if self.mode == "terminal":
            self.logger.warning(inputstr)
        elif self.mode == "frontend":
            print("warning : " + inputstr)

    def error(self, inputstr):
        if self.mode == "terminal":
            self.logger.error(inputstr)
        elif self.mode == "frontend":
            print("error : " + inputstr)


# 只能实例化一次，避免handler的重复添加，导致多重输出
# 调用方法：from general_basic.log import logger_re as logger
logger_re = LogRepack()
logger_raw = logger_re.get_raw()
