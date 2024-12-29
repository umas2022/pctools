'''
rog台式机备份d盘和e盘
'''
import sys, os
script_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(script_path)
from functions import *

input_json = {
    "path_in": r"D:\\",
    "path_out": r"F:\\backup-data",
    # 是否计数
    "if_count": False,
}


copy_with_structure(input_json)
