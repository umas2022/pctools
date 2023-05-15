'''
常用的path函数
注意normpath会将空字符替换为"."
'''

import os


def unorm(path):
    '''格式统一'''
    return os.path.normpath(path)


def ujoin(path1,path2):
    '''路径合并'''
    return unorm(os.path.join(path1,path2))


