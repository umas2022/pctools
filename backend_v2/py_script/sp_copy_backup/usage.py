
import sys
sys.path.append("..")
from sp_copy_backup.copy_backup import CopyBackup


# path_in = r'D:\s-linux\project\test_file\test_in'
# path_out = r'D:\s-linux\project\test_file\test_out'


json_set = {
    "path_in": r'G:\内部存储\Tachiyomi',
    "path_out": r'D:\s-workspace\Tachiyomi',
    "path_log": r'D:\s-linux\project\test_file\test_log',
    "keyword": r".cbz"
}


vc = CopyBackup(json_set=json_set)
vc.run()
