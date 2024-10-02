import sys
import os
script_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(script_path)
from sp_remove_duplicate.duplicate_rm import DuplicateRm as MainClass


json_set = {
    'path_in': r'D:\s-code\test\test_in',
    'path_log': "",
    'filter_1': "dimension",
    'filter_2': "hash",
    "iter_level": "all",
    "cut_mode": True,
    "cut_path": r"",
    "if_count": False,
}

vc = MainClass(json_set)
vc.run()
