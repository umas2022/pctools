
import sys
sys.path.append("..")
from sp_compress_7zip import MainClass


json_set = {
    "method": "exe",
    "path_in": "D:\\s-code\\test\\test_in",
    "path_out": "D:\\s-code\\test\\test_out",
    "password": "",
    "path_log": "D:\\s-code\\test\\test_log",
    "path_7z": "D:\\p-program\\7zip\\7-Zip\\7z.exe",
    "th_total": 1,
    "overwrite": False,
    "keyword": "#",
    "location": "0",
    "double_cp": True,
    "deep": True
}
vc = MainClass(json_set=json_set)

vc.run()
