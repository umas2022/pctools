'''
create: 2022.9.20

sp包入口
'''

import json
from utils_logger.log import logger_re as logger
from sp_compress_video.video_compress import VideoCompress
from sp_compress_image.img_compress import ImgCompress
from sp_copy_merge.copy_merge import CopyMerge


class SpManager():
    '''sp包入口, run函数额外提供json格式的输入'''

    def __init__(self) -> None:
        pass

    def run_compress_image(self, path_in="", path_out="", path_log="", max_size_kb=3072, json_set={}):
        '''图片压缩\n
        path_in: 输入路径\n
        path_out: 输出路径\n
        path_log: log文件路径(可选)\n
        max_size_kb: 图片大小限制(默认3072KB)'''
        if not json_set == {}:
            path_in = json_set['path_in']
            path_out = json_set['path_out']
            path_log = json_set['path_log'] if "path_log" in json_set else ""
            max_size_kb = json_set['max_size_kb'] if "max_size_kb" in json_set else 3072
        ic = ImgCompress(path_in, path_out, path_log, max_size_kb)
        ic.run()

    def run_compress_video(self, path_in="", path_out="", path_log="", max_bit_kbps=10000, cpu_thread=3, json_set={}):
        '''视频压缩\n
        path_in: 输入路径\n
        path_out: 输出路径\n
        path_log: log文件路径(可选)\n
        max_bit_kbps: 最大比特率(默认10000kbps)\n
        cpu_thread: cpu占用量(6核cpu, 默认thread=3, 占用率50%)'''
        if not json_set == {}:
            path_in = json_set['path_in']
            path_out = json_set['path_out']
            path_log = json_set['path_log'] if "path_log" in json_set else "1"
            max_bit_kbps = json_set['max_bit_kbps'] if "max_bit_kbps" in json_set else 10000
            cpu_thread = json_set['cpu_thread'] if "cpu_thread" in json_set else 3
        vc = VideoCompress(path_in, path_out, path_log, max_bit_kbps, cpu_thread)
        vc.run()

    def run_copy_merge(self, path_in="", path_out="", json_set={}):
        '''拷贝合并\n
        path_in: 输入路径\n
        path_out: 输出路径'''
        if not json_set == {}:
            path_in = json_set['path_in']
            path_out = json_set['path_out']
        cm = CopyMerge(path_in, path_out)
        cm.run()

    def quick_start(self, pre_key: str):
        '''使用preset.json中的预设参数快速运行函数'''
        preset_dic = json.load(open("./preset.json", "r", encoding="utf-8"))
        if not pre_key in preset_dic:
            logger.error("sp-manager: unexpected key - %s" % pre_key)
        preset_one = preset_dic[pre_key]
        if not preset_one["function"] in dir(self):
            logger.error("sp-manager: unexpected function - %s" % preset_one["function"])
        called_func = getattr(self, preset_one["function"])
        called_func(json_set=preset_one["input"])
