'''
create: 应该早于2022.10.1
sp_operator的终端启动器
'''

import sys
import os
import json
import time

this_path = os.path.split(os.path.realpath(__file__))[0]
server_path = os.path.dirname(this_path)
pctools_path = os.path.dirname(server_path)
script_path = os.path.join(pctools_path,"py_script")
sys.path.append(pctools_path)
sys.path.append(script_path)

from py_script.sp_manager import SpManager
from py_script.sp_manager import logger

now = time.time()

text_data = sys.argv[1]
get_data = json.loads(text_data)
get_function = get_data["function"]

sm = SpManager()
if not get_function in dir(sm):
    logger.error("sp-manager: unexpected function - %s" % get_function)
    exit(1)
called_func = getattr(sm, get_function)
called_func(json_set=get_data)

time_spent_ms = int(1000 * (time.time() - now))
time_spent = str(time_spent_ms / 1000) + "s" if time_spent_ms > 1000 else str(time_spent_ms) + "ms"
logger.info("time-spent: %s" % time_spent)

wait_here = input("\n\nprocess finish, press enter to exit ...")
