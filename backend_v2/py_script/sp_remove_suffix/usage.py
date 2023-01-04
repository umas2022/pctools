
import sys
sys.path.append("..")
from sp_remove_suffix.remove_suffix import RemoveSuffix


# path_in = r'D:\s-linux\project\test_file\test_in'
# keyword = "DOC"
path_in = r"D:\s-linux\project\test_file\test_out"
suffix = "xls"


rs = RemoveSuffix(path_in,suffix)
rs.run()