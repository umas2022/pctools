
import os


class Traverse():
    def __init__(self) -> None:
        pass

    def get_file(path_in):
        '''文件遍历'''
        for root, dirs, files in os.walk(path_in):
            for fileName in files:
                full_path = os.path.join(root, fileName).replace('\\', "/")
                yield full_path
