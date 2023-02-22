
import os
from utils_logger.log import logger_re as logger


class Traverse():
    '''文件夹遍历类,记得加括号实例化Traverse().getfile()'''
    def __init__(self) -> None:
        pass

    def onerror(self, err):
        logger.error("get file error : %s" % err)

    def get_file(self, path_in):
        '''文件遍历'''
        for root, dirs, files in os.walk(path_in, onerror=self.onerror):
            for fileName in files:
                full_path = os.path.join(root, fileName).replace('\\', "/")
                yield full_path

    def get_dir(self, path_in):
        '''文件夹遍历:返回所有层级文件夹'''
        for root, dirs, files in os.walk(path_in, onerror=self.onerror):
            for dir in dirs:
                full_path = os.path.join(root, dir).replace('\\', "/")
                yield full_path

    def get_first_dir(self,path_in):
        '''文件夹遍历:只返回第一层文件夹'''
        for dir in os.listdir(path_in):
            full_path = os.path.join(path_in, dir).replace('\\', "/")
            if os.path.isdir(full_path):
                yield full_path


                