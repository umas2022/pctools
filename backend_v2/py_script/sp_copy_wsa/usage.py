
import sys
sys.path.append("..")
from sp_copy_wsa.copy_wsa import CopyWsa


json_set = {
    "path_adb": r'D:\\p-tools\\platform-tools\\adb.exe',
    "adb_port": r'127.0.0.1:58526',
    "path_in": r'D:\s-linux\project\test_file\test_in',
    "path_out": r'/sdcard/Download/',
    "path_log": r'D:\s-linux\project\test_file\test_log',
    "keyword": r""
}


vc = CopyWsa(json_set=json_set)
vc.run()
