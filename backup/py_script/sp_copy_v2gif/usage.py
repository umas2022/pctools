import sys,os
script_path =os.path.dirname(os.path.dirname(os.path.realpath(__file__))) 
sys.path.append(script_path)
from sp_copy_v2gif.copy_v2gif import Video2Gif as MainClass


json_set = {
    'path_in': r'D:\p-Huawei\Huawei Share',
    'path_out': r'D:\p-Huawei\HuaweiShare2',
    'path_log': "",
    'if_count': True,
    "fps":15,
    "size_w":0,
    "size_h":0,
}

vc = MainClass(json_set)
vc.run()
