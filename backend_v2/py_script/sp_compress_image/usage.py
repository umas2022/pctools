
import sys
sys.path.append("..")
from sp_compress_image.img_compress import ImgCompress


# path_in = r"D:\s-linux\project\test_file\test_in"
# path_out = r"D:\s-linux\project\test_file\test_out"
# vc = ImgCompress(path_in,path_out)


path_in = r'D:\s-linux\project\test_file\test_in'
path_out = r'D:\s-linux\project\test_file\test_in'
path_log = r""
vc = ImgCompress(path_in,path_out,path_log,4000)

vc.run()