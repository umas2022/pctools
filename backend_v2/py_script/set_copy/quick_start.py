import json
import os
import sys
from utils_logger.log import logger_re as logger
import pkgutil
import importlib


class QuickStart:
    def __init__(self, pre_key="", json_set={}) -> None:
        '''使用preset.json中的预设参数快速运行函数'''
        self.pre_key = pre_key
        if not json_set == {}:
            try:
                self.pre_key = json_set['pre_key']
            except Exception as e:
                logger.error("key error: %s" % e)
                return
        logger.debug(self.pre_key)

    def run(self):
        # 读取json文件
        script_path = os.path.split(os.path.realpath(__file__))[0]
        preset_path = os.path.join(script_path, "./preset.json")
        preset_dic = json.load(open(preset_path, "r", encoding="utf-8"))

        # 匹配预设方法名
        if not self.pre_key in preset_dic:
            logger.error("quick_start: unexpected key - %s" % self.pre_key)
            exit(0)
        preset_select = preset_dic[self.pre_key]
        if "path_log" in preset_select:
            logger.set_path(preset_select["path_log"])

        # 逐步运行
        for step in preset_select["action"]:
            # 引入目标函数
            mc = ""
            py_path = os.path.abspath(os.path.join(os.path.split(os.path.realpath(__file__))[0], ".."))
            for filefiner, name, ispkg in pkgutil.iter_modules([py_path]):
                if name == step["function"]:
                    importlib.import_module(name)
                    module = sys.modules[name]
                    mc = module.MainClass(json_set=step["input"])
                    break
            if mc == "":
                logger.error("quick_start: unexpected function - %s" % step["function"])
                exit(0)
            else:
                mc.run()
