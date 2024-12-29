import sys, os

script_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(script_path)
from sp_copy_merge.copy_merge import CopyMerge as MainClass

# base_path = r"E:\[M2]-samu\wfs\Sirfy作品合集\Sirfy"

json_set = {
    'path_in': r'D:\save-samu\apc\[Alpha]-pe-\pk',
    'path_out': r'D:\save-samu\apc\[Alpha]-pe-\ex',
    # "path_in": base_path,
    # "path_out": base_path + "x",
    "path_log": "",
    "if_count": False,
    "if_inner": False
}

vc = MainClass(json_set)
vc.run()
