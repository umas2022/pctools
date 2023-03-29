
import sys
sys.path.append("..")
from sp_compress_image.img_compress import ImgCompress



path_in = r'D:\s-code\test\test_in'
path_out = r'D:\s-code\test\test_in'
path_log = r""
vc = ImgCompress(path_in,path_out,path_log,500)

vc.run()