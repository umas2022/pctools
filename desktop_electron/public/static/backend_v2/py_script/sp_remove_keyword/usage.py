
import sys
sys.path.append("..")
from sp_remove_keyword.remove_keyword import RemoveKeyword


# path_in = r'D:\s-linux\project\test_file\test_in'
# keyword = "DOC"
path_in = r"D:\d-telegram\tama2"
keyword = "_1"


rk = RemoveKeyword(path_in,keyword)
rk.run()