
import sys
sys.path.append("..")
from sp_remove_difference.remove_difference import RemoveDifference


# json_set = {
#     "base_path": r'D:\s-code\test\test_in',
#     "del_path": r'D:\s-code\test\test_out',
#     "log_path": r'D:\s-code\test\test_out\log'
# }

json_set = {
    "base_path": r'V:',
    "del_path": r'W:',
    "log_path": r'D:\s-code\test\test_out\log',
    "if_count": False
}


rd = RemoveDifference(json_set)
rd.run()
