
import sys
sys.path.append("..")
from sp_copy_check.copy_check import CopyCheck


path_in = r'D:\s-code\test\test_in'
path_out = r'D:\s-code\test\test_out'

cc = CopyCheck(path_in,path_out)
cc.run()