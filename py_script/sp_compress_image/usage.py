
import sys
sys.path.append("..")
from sp_compress_image.img_compress import ImgCompress


# path_in = r"D:\s-linux\project\test_file\test_in"
# path_out = r"D:\s-linux\project\test_file\test_out"
path_in = r'E:\[2T]-samu-raw'
path_out = r'F:\[1T]-samu-cut'
vc = ImgCompress(path_in,path_out)
vc.run()