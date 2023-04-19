import sys,os
script_path =os.path.dirname(os.path.dirname(os.path.realpath(__file__))) 
sys.path.append(script_path)
from sp_rename_basic.rename_basic import RenameBasic as MainClass


path_in = r'D:\s-code\test\test_out'
json_set = {
    "path_in": "D:\\s-code\\test\\test_out",
    "use_func": "num_array",
    "target": "dir",
    "add_in": "4",
    "add_in_2": "21"
}

vc = MainClass(json_set=json_set)
vc.run()
