

import sys,os
script_path =os.path.dirname(os.path.dirname(os.path.realpath(__file__))) 
sys.path.append(script_path)
from sp_copy_backup.copy_backup import CopyBackup as MainClass

json_set = {
    "path_in": r'D:\s-code\test\test_in',
    "path_out": r'D:\s-code\test\test_out',
    "path_log": r'D:\s-code\test\test_log',
    "if_count": False,
    "check_size": True,
    # "keyword": r"txt",
    # "location": r"-1"
}


vc = MainClass(json_set=json_set)
vc.run()
