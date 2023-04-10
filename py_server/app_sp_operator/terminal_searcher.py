'''
create: 2022.11.1
终端模式启动器
'''
import sys
import os
import json
import time
import pkgutil
import importlib

this_path = os.path.split(os.path.realpath(__file__))[0]
server_path = os.path.dirname(this_path)
pctools_path = os.path.dirname(server_path)
script_path = os.path.join(pctools_path,"py_script")
sys.path.append(pctools_path)
sys.path.append(script_path)

from py_script.utils_logger.log import logger_re as logger

now = time.time()

text_data = sys.argv[1]
get_data = json.loads(text_data)
get_function = get_data["function"]

for filefiner,name,ispkg in pkgutil.iter_modules([get_data["py_path"]]):
    if name == get_data["function"]:
        importlib.import_module(name)
        module = sys.modules[name]
        mc = module.MainClass(json_set = get_data)
        mc.run()

time_spent_ms = int(1000 * (time.time() - now))
time_spent = str(time_spent_ms / 1000) + "s" if time_spent_ms > 1000 else str(time_spent_ms) + "ms"
logger.info("time-cost: %s" % time_spent)

wait_here = input("\n\nprocess finish, press enter to exit ...")
