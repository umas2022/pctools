
import sys
sys.path.append("..")
from sp_compress_7zip_exe.archive_7z import Archive7z


json_set = {
    "path_in": r'D:\s-linux\project\test_file\test_in',
    "path_out": r'D:\s-linux\project\test_file\test_out',
    "path_log": r"",
    "path_7z": r"D:\\p-program\\7zip\\7-Zip\\7z.exe",
    "password": "umas1970",
    "th_total": "3",
    "overwrite": False
}
vc = Archive7z(json_set=json_set)

vc.run()
