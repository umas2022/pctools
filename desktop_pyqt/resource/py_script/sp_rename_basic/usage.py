
import sys
sys.path.append("..")
from sp_rename_basic.rename_basic import RenameBasic


path_in = r'D:\s-code\test\test_in'
# use_func = "add_prefix"
use_func = "del_prefix"
add_in = "prefix_"
vc = RenameBasic(path_in=path_in, use_func=use_func, add_in=add_in)
vc.run()
