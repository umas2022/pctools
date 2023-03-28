

import os
import sys
py_path = os.path.split(os.path.realpath(__file__))[0]
script_path = os.path.split(py_path)[0]
sys.path.append(script_path)
from sp_copy_backup.copy_backup import CopyBackup

json_set = {
    "path_in": r'D:\s-code\test\test_in',
    "path_out": r'D:\s-code\test\test_out',
    "path_log": r'D:\s-code\test\test_log',
    "keyword": r"txt",
    "location": r"-1"
}

# json_set = {
#     "path_in": r'G:\内部存储\Tachiyomi',
#     "path_out": r'D:\s-workspace\Tachiyomi',
#     "path_log": r'D:\s-code\test\test_log',
#     "keyword": r".cbz",
#     "location": r"-1"
# }


vc = CopyBackup(json_set=json_set)
vc.run()
