
import sys
sys.path.append("..")
from sp_compress_video.video_compress import VideoCompress


path_in = r'E:\[2T]-samu-raw'
path_out = r'F:\[1T]-samu-cut'
path_log = r'F:\[1T]-samu-cut\log'
vc = VideoCompress(path_in,path_out,path_log)
vc.run()