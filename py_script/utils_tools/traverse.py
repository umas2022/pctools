
import os
from utils_logger.log import logger_re as logger


class Traverse():
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
