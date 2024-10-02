'''
文件夹遍历类,记得加括号实例化Traverse().getfile() \n
注意遍历以文件名字符串排序输出,不能自动排序多位数字 \n
即 1,10,2,3...8,9;应该先对不齐的位置补零
'''


import os
from utils_logger.log import logger_re as logger


class Traverse():
    '''文件夹遍历类,记得加括号实例化Traverse().getfile() \n
    注意遍历以文件名字符串排序输出,不能自动排序多位数字 \n
    即 1,10,2,3...8,9;应该先对不齐的位置补零'''

    def __init__(self) -> None:
        pass

    def onerror(self, err):
        logger.error("Traverse get file error : %s" % err)

    def get_file(self, path_in):
        '''文件遍历'''
        for root, dirs, files in os.walk(path_in, onerror=self.onerror):
            for fileName in files:
                full_path = os.path.normpath(os.path.join(root, fileName))
                yield full_path

    def get_dir(self, path_in):
        '''文件夹遍历:返回所有层级文件夹'''
        for root, dirs, files in os.walk(path_in, onerror=self.onerror):
            for dir in dirs:
                full_path = os.path.normpath(os.path.join(root, dir))
                yield full_path

    def get_first_dir(self, path_in):
        '''文件夹遍历:只返回第一层文件夹'''
        items = os.listdir(path_in)
        items_sorted = sorted(items)
        for item in items_sorted:
            full_path = os.path.normpath(os.path.join(path_in, item))
            if os.path.isdir(full_path):
                yield full_path

    def get_first_file(self, path_in):
        '''文件遍历:只返回第一层文件'''
        items = os.listdir(path_in)
        items_sorted = sorted(items)
        for item in items_sorted:
            full_path = os.path.normpath(os.path.join(path_in, item))
            if not os.path.isdir(full_path):
                yield full_path
