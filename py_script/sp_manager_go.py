'''
create: 2022.9.20

桌面端调用入口
'''

import sys
import json
from utils_logger.log import logger_re as logger
from sp_manager import SpManager

# pyshell传参从1开始，0位是脚本路径
# print(sys.argv[1])
logger.set_mode("frontend")

# func_name = sys.argv[1]
# input_set = json.loads(sys.argv[2])
# sm = SpManager()
# if not func_name in dir(sm):
#     logger.error("sp-go: unexpected function - %s" % func_name)
#     exit(0)

# called_func = getattr(sm, func_name)
# # called_func(json_set=input_set)


logger.info(str("完成！".encode("utf-8")))
