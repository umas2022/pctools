
import sys
sys.path.append("..")
from sp_copy_backup.copy_backup import CopyBackup


path_in = r'D:\s-linux\project\test_file\test_in'
path_out = r'D:\s-linux\project\test_file\test_out'

vc = CopyBackup(path_in,path_out)
vc.run()