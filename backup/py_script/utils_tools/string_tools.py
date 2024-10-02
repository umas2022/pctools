'''
create: 2023.2.17

字符串处理工具合集
'''

import os
from utils_logger.log import logger_re as logger


class StringTools():
    '''字符串处理类,StringTools().getfile()'''
    def __init__(self) -> None:
        pass

    def onerror(self, err):
        logger.error("get file error : %s" % err) 

    def location_match(self,template:str,keyword:str,location:int)->bool:
        '''判断字符串位置,location=[0,1,2, ... ,-2,-1]\n
        负数的匹配计入keyword长度,如在"file.txt"中匹配".tx"结果是-2,匹配".txt"结果是-1'''
        # 负数位置换算
        if location<0:
            location = len(template)+location-len(keyword)+1
        find_loca = template.find(keyword)
        # 字符串不存在
        if find_loca == -1:
            return False
        # 循环匹配目标位置
        while not find_loca == location:
            find_loca = template.find(keyword,find_loca+1)
            if find_loca == -1:
                return False
        return True
        

                