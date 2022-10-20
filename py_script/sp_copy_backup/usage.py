
import sys
sys.path.append("..")
from sp_copy_backup.copy_backup import CopyBackup


path_in = r'D:\s-linux\project\test_file\test_in'
path_out = r'D:\s-linux\project\test_file\test_out'


path_in = r'此电脑\HUAWEI MatePad Pro\内部存储\Tachiyomi'
path_out = r'D:\s-workspace\新建文件夹\Tachiyomi'

vc = CopyBackup(path_in,path_out)
vc.run()