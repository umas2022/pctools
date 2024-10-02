import sys,os
script_path =os.path.dirname(os.path.dirname(os.path.realpath(__file__))) 
sys.path.append(script_path)
from sp_copy_split.copy_split import CopySplit as MainClass


json_set = {
    'path_in': r'D:\s-code\test\test_in',
    'path_out': r'D:\s-code\test\test_out',
    'path_log': "",
    "if_count":True,
    'single_cap': 3,
    'name_func': "by_num",
    'if_count': False
}

vc = MainClass(json_set)
vc.run()
