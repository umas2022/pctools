import sys,os
script_path =os.path.dirname(os.path.dirname(os.path.realpath(__file__))) 
sys.path.append(script_path)
from sp_copy_v2gif.copy_v2gif import Video2Gif as MainClass


json_set = {
    'path_in': r'D:\s-code\test\test_in',
    'path_out': r'D:\s-code\test\test_out',
    'path_log': "",
    'if_count': False,
    "fps":15,
    "size_w":0,
    "size_h":0,
}

vc = MainClass(json_set)
vc.run()
