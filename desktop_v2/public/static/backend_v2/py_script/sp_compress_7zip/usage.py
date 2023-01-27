
import sys
sys.path.append("..")
from sp_compress_7zip.archive_7z import Archive7z



path_in = r'D:\s-linux\project\test_file\test_in'
path_out = r'D:\s-linux\project\test_file\test_in'
password = "umas1970"
path_log = r""
vc = Archive7z(path_in=path_in, path_out=path_out, password=password, path_log=path_log)

vc.run()
