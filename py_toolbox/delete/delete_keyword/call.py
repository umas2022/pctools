'''
删除关键字
'''
import sys, os
script_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(script_path)
from functions import *

input_json = {
        "path_in": r"D:\self-code\test\test_in",
        "path_out": r"",
        # 是否计数
        "if_count": True,
        # 是否拷贝
        "if_copy": False,
        # 关键字列表
        "keywords": ["_1.","_2.","_3.","_4."]
}


copy_or_delete_files(input_json)
