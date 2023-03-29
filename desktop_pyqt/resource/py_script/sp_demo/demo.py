import json
import os
import sys
from utils_logger.log import logger_re as logger
import pkgutil
import importlib


class SpDemo:
    def __init__(self, json_set={}) -> None:
        '''使用preset.json中的预设参数快速运行函数'''
        try:
            self.dm_input = json_set['dm_input']
            self.dm_select = json_set['dm_select']
            self.dm_switch = bool(json_set['dm_switch']) 
            self.dm_input2 = json_set['dm_input2'] if "dm_input2" in json_set else ""

        except Exception as e:
            logger.error("key error: %s" % e)
            return
        
    def dm_button(self):
        '''按钮'''
        logger.debug("按钮被调用了")

    def run(self):
        logger.debug("获取参数:")
        logger.debug("dm_input : %s" % self.dm_input)
        logger.debug("dm_select : %s" % self.dm_select)
        logger.debug("dm_switch : %s" % self.dm_switch)
        logger.debug("dm_input2 : %s" % self.dm_input2)
