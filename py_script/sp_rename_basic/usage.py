
import sys
sys.path.append("..")
from sp_rename_basic.rename_basic import RenameBasic


path_in = r'D:\s-code\test\test_out'
json_set = {
    "path_in": "D:\\s-code\\test\\test_out",
    "use_func": "replace_key",
    "target": "file",
    "add_in": "_cp2",
    "add_in_2": ""
}

vc = RenameBasic(json_set=json_set)
vc.run()
