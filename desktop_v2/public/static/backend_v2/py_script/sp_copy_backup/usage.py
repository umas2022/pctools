
import sys
sys.path.append("..")
from sp_copy_backup.copy_backup import CopyBackup


# path_in = r'D:\s-linux\project\test_file\test_in'
# path_out = r'D:\s-linux\project\test_file\test_out'


path_out = r'F:\内部存储\Tachiyomi'
path_in = r'D:\s-workspace\新建文件夹\Tachiyomi'
path_log = r'D:\s-workspace\新建文件夹\log'

vc = CopyBackup(path_in,path_out,path_log)
vc.run()