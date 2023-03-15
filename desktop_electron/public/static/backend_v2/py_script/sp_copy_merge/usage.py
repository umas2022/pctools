
import sys
sys.path.append("..")
from sp_copy_merge.copy_merge import CopyMerge


# path_in = r'D:\s-linux\project\test_file\test_in'
# path_out = r'D:\s-linux\project\test_file\test_out'
path_in = r"D:\s-samu\wfs\あらた作品合集\あらた"
path_out = r"D:\s-samu\wfs\あらた作品合集\[あらた]"

vc = CopyMerge(path_in,path_out)
vc.run()