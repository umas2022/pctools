
import sys
sys.path.append("..")
from sp_remove_difference.remove_difference import RemoveDifference


base_path = r'D:\s-code\test\test_in'
del_path = r'D:\s-code\test\test_out'
log_path = r'D:\s-code\test\test_out\log'

rd = RemoveDifference(base_path, del_path,log_path)
rd.run()
