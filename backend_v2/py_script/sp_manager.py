'''
create: 2022.9.20

sp包入口
每个函数除基本输入外都配备json_set输入, 用于后端直接调用

2022.11.1 改用后端直接搜索py_script目录, 此入口函数不再更新
已经用新写法重置的函数在下面注释了
'''

import json
import os
import sys
from utils_logger.log import logger_re as logger
from sp_compress_video.video_compress import VideoCompress
from sp_compress_image.img_compress import ImgCompress
from sp_copy_backup.copy_backup import CopyBackup
from sp_copy_check.copy_check import CopyCheck
from sp_copy_merge.copy_merge import CopyMerge
from sp_remove_difference.remove_difference import RemoveDifference
from sp_remove_keyword.remove_keyword import RemoveKeyword
from sp_remove_suffix.remove_suffix import RemoveSuffix
from sp_rename_basic.rename_basic import RenameBasic


class SpManager():
    '''sp包入口, run函数额外提供json格式的输入'''

    def __init__(self) -> None:
        pass

    # def run_compress_image(self, path_in="", path_out="", path_log="", max_size_kb=3072, json_set={}):
    #     '''压缩：图片压缩\n
    #     path_in: 输入路径\n
    #     path_out: 输出路径\n
    #     path_log: log文件路径(可选)\n
    #     max_size_kb: 图片大小限制(默认3072KB)'''
    #     if not json_set == {}:
    #         try:
    #             path_in = json_set['path_in']
    #             path_out = json_set['path_out']
    #             path_log = json_set['path_log'] if "path_log" in json_set else ""
    #             max_size_kb = int(json_set['max_size_kb']) if "max_size_kb" in json_set else 3072
    #         except Exception as e:
    #             logger.error("key error: %s" %e)
    #             return
    #     ic = ImgCompress(path_in, path_out, path_log, max_size_kb)
    #     ic.run()

    # def run_compress_video(self, path_in="", path_out="", path_log="", max_bit_kbps=10000, cpu_thread=3, json_set={}):
    #     '''压缩：视频压缩\n
    #     path_in: 输入路径\n
    #     path_out: 输出路径\n
    #     path_log: log文件路径(可选)\n
    #     max_bit_kbps: 最大比特率(默认10000kbps)\n
    #     cpu_thread: cpu占用量(6核cpu, 默认thread=3, 占用率50%)'''
    #     if not json_set == {}:
    #         try:
    #             path_in = json_set['path_in']
    #             path_out = json_set['path_out']
    #             path_log = json_set['path_log'] if "path_log" in json_set else ""
    #             max_bit_kbps = int(json_set['max_bit_kbps'])  if "max_bit_kbps" in json_set else 10000
    #             cpu_thread = int(json_set['cpu_thread']) if "cpu_thread" in json_set else 3
    #         except Exception as e:
    #             logger.error("key error: %s" %e)
    #             return
    #     vc = VideoCompress(path_in, path_out, path_log, max_bit_kbps, cpu_thread)
    #     vc.run()

    # def run_copy_backup(self, path_in="", path_out="", path_log="", json_set={}):
    #     '''拷贝：完全备份\n
    #     path_in: 输入路径\n
    #     path_out: 输出路径'''
    #     if not json_set == {}:
    #         try:
    #             path_in = json_set['path_in']
    #             path_out = json_set['path_out']
    #             path_log = json_set['path_log'] if "path_log" in json_set else ""
    #         except Exception as e:
    #             logger.error("key error: %s" %e)
    #             return
    #     cb = CopyBackup(path_in, path_out, path_log)
    #     cb.run()

    # def run_copy_merge(self, path_in="", path_out="", path_log="", json_set={}):
    #     '''拷贝：拷贝合并\n
    #     path_in: 输入路径\n
    #     path_out: 输出路径'''
    #     if not json_set == {}:
    #         try:
    #             path_in = json_set['path_in']
    #             path_out = json_set['path_out']
    #             path_log = json_set['path_log'] if "path_log" in json_set else ""
    #         except Exception as e:
    #             logger.error("key error: %s" %e)
    #             return
    #     cm = CopyMerge(path_in, path_out, path_log)
    #     cm.run()

    def run_copy_check(self, path_in="", path_out="", path_log="", json_set={}):
        '''拷贝：结果检查\n
        path_in: 输入路径\n
        path_out: 输出路径'''
        if not json_set == {}:
            try:
                path_in = json_set['path_in']
                path_out = json_set['path_out']
                path_log = json_set['path_log'] if "path_log" in json_set else ""
            except Exception as e:
                logger.error("key error: %s" %e)
                return
        cc = CopyCheck(path_in, path_out, path_log)
        cc.run()

    # def run_remove_difference(self, base_path="", del_path="", path_log="", json_set={}):
    #     '''删除：删除差异\n
    #     path_in: 输入路径\n
    #     path_out: 输出路径'''
    #     if not json_set == {}:
    #         try:
    #             base_path = json_set['base_path']
    #             del_path = json_set['del_path']
    #             path_log = json_set['path_log']if "path_log" in json_set else ""
    #         except Exception as e:
    #             logger.error("key error: %s" %e)
    #             return
    #     rd = RemoveDifference(base_path, del_path, path_log)
    #     rd.run()

    # def run_remove_keyword(self, path_in="", keyword="", path_log="", json_set={}):
    #     '''删除：删除关键字\n
    #     path_in: 输入路径\n
    #     path_out: 输出路径'''
    #     if not json_set == {}:
    #         try:
    #             path_in = json_set['path_in']
    #             keyword = json_set['keyword']
    #             path_log = json_set['path_log']if "path_log" in json_set else ""
    #         except Exception as e:
    #             logger.error("key error: %s" %e)
    #             return
    #     rk = RemoveKeyword(path_in, keyword, path_log)
    #     rk.run()

    def run_remove_suffix(self, path_in="", suffix="", path_log="", json_set={}):
        '''删除：删除后缀名\n
        path_in: 输入路径\n
        suffix: 指定后缀名'''
        if not json_set == {}:
            try:
                path_in = json_set['path_in']
                suffix = json_set['suffix']
                path_log = json_set['path_log']if "path_log" in json_set else ""
            except Exception as e:
                logger.error("key error: %s" %e)
                return
        rs = RemoveSuffix(path_in, suffix, path_log)
        rs.run()

    # def run_rename_basic(self, path_in="", use_func="", add_in="", path_log="", json_set={}):
    #     '''基础重命名\n
    #     path_in: 输入路径\n
    #     use_func: 重命名方法
    #     add_in: 附加输入参数
    #     path_log: 日志路径(置空不使用日志)'''
    #     if not json_set == {}:
    #         try:
    #             path_in = json_set['path_in']
    #             use_func = json_set['use_func']
    #             add_in = json_set['add_in']
    #             path_log = json_set['path_log']if "path_log" in json_set else ""
    #         except Exception as e:
    #             logger.error("key error: %s" %e)
    #             return
    #     rb = RenameBasic(path_in, use_func, add_in, path_log)
    #     rb.run()

    # def quick_start(self, pre_key="", json_set={}):
    #     '''使用preset.json中的预设参数快速运行函数'''
    #     if not json_set == {}:
    #         try:
    #             pre_key = json_set['pre_key']
    #         except Exception as e:
    #             logger.error("key error: %s" %e)
    #             return
    #     script_path = os.path.split(os.path.realpath(__file__))[0]
    #     preset_path = os.path.join(script_path, "./preset.json")
    #     preset_dic = json.load(open(preset_path, "r", encoding="utf-8"))
    #     if not pre_key in preset_dic:
    #         logger.error("sp-manager: unexpected key - %s" % pre_key)
    #         exit(0)
    #     preset_select = preset_dic[pre_key]
    #     if "path_log" in preset_select:
    #         logger.set_path(preset_select["path_log"])
    #     for step in preset_select["action"]:
    #         if not step["function"] in dir(self):
    #             logger.error("sp-manager: unexpected function - %s" % step["function"])
    #             exit(0)
    #         called_func = getattr(self, step["function"])
    #         called_func(json_set=step["input"])


