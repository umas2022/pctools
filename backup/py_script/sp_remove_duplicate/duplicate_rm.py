'''
create: 2023.7.9
图片查重
'''


import json
from PIL import Image
import imagehash  # pip install imagehash
from collections import defaultdict
import cv2
import numpy as np
import skimage.metrics
import skimage.measure
import time
from typing import Callable
import os
import shutil
from utils_logger.log import logger_re as logger
from utils_tools.traverse import Traverse
from utils_tools.traverse_copy import TVcopy


class DuplicateRm(TVcopy):
    def __init__(self, json_set={}) -> None:
        try:
            # 目标路径
            self.path_in = os.path.normpath(json_set['path_in'])
            # * 如果日志路径包含在被删除目录中,将被直接跳过不作删除
            self.path_log = os.path.normpath(json_set['path_log']) if "path_log" in json_set else ""
            self.path_log = "" if self.path_log == "." else self.path_log
            logger.set_path(self.path_log)
            # 预筛方法["hash","size","dimension"]
            self.filter_chain = ["", ""]
            self.filter_chain[0] = json_set['filter_1'] if "filter_1" in json_set else ""
            # 复筛方法["hash","size","dimension"]
            self.filter_chain[1] = json_set['filter_2'] if "filter_2" in json_set else ""
            # 试错模式,启用后目标将被移动到试错目录,而不是直接删除[True,False]
            self.cut_mode = bool(json_set['cut_mode']) if "cut_mode" in json_set else False
            # 遍历层级（全层级/仅第一层）["first","all"]
            self.iter_level = json_set['iter_level'] if "iter_level" in json_set else "first"
            # 试错目录,置空不使用试错模式
            self.cut_path = os.path.normpath(json_set['cut_path']) if "cut_path" in json_set else ""
            self.path_out = self.cut_path
            # 程序控制:是否计数(默认True)[True,False]
            self.if_count = bool(json_set['if_count']) if "if_count" in json_set else True
            TVcopy.__init__(self, self.path_in, self.path_out, self.path_log, self.if_count)
        except Exception as e:
            logger.error("key error: %s" % e)
            return

        # 所有图片列表，格式 [[path_1,path_2],[path_1,path2],[path_1,path_2]]，用于遍历查重
        self.image_path_list = [[]]
        self.total = len(self.image_path_list[0])
        # 重复图片列表，格式同上，用于删除
        self.duplicate_list = []

    def filter_entrance(self, image_paths: list, feature_func: Callable, func_name: str, process_str: str) -> list:
        '''过滤器外壳，套在不同的特征筛选方法上'''
        image_hashes = defaultdict(list)
        duplicate_dict = defaultdict(list)
        total = len(image_paths)
        now = 0
        for image_path in image_paths:
            now += 1
            try:
                image = Image.open(image_path)
                image_hash = feature_func(image)
                image_hashes[image_hash].append(image_path)
                if len(image_hashes[image_hash]) > 1:
                    duplicate_dict[image_hash] = list(set(duplicate_dict[image_hash] + image_hashes[image_hash]))
                    logger.info("\n==> find duplicate : (%s) %d/%d %s" % (func_name, now, total, process_str))
                    for item in duplicate_dict[image_hash]:
                        logger.info(item)
            except Exception as err:
                logger.error("Image.open error: %s" % err)
        duplicate_list = [image_list for image_list in duplicate_dict.values()]
        return duplicate_list

    def __dim_filter(self, image_paths, process_str):
        '''筛选方法：寻找相同图片(尺寸)'''
        def filter_func(image):
            width, height = image.size
            image_dim = str(width) + "-" + str(height)
            return image_dim
        return self.filter_entrance(image_paths, filter_func, "dimension", process_str)

    def __hash_filter(self, image_paths, process_str):
        '''筛选方法：寻找相同图片(哈希)'''
        def filter_func(image):
            return imagehash.phash(image)
        return self.filter_entrance(image_paths, filter_func, "hash", process_str)

    def __size_filter(self, image_paths, process_str):
        '''筛选方法：寻找相同图片(体积)'''
        def filter_func(image):
            return os.path.getsize(image)
        return self.filter_entrance(image_paths, filter_func, "size", process_str)

    def main_filter(self):
        '''分类查重主函数'''
        source_list = self.image_path_list
        duplicate_list = []

        for filter in self.filter_chain:
            if filter == "hash":
                filter_func = self.__hash_filter
            elif filter == "size":
                filter_func = self.__size_filter
            elif filter == "dimension":
                filter_func = self.__dim_filter
            else:
                logger.error("unexpected filter : %s" % filter)
                return

            total = len(source_list)
            now = 0
            for each_group in source_list:
                now += 1
                duplicate_list_add = filter_func(each_group, "%d/%d" % (now, total))
                duplicate_list += duplicate_list_add if not duplicate_list_add == [] else []

            source_list = duplicate_list
            duplicate_list = []
        self.duplicate_list = source_list
        logger.info("\nFind %d sets of duplicate images.\nPress Button to delete duplicate images \nIt is recommended to use cut_mode before delete ..." % len(self.duplicate_list))

    def rm_dp(self):
        '''删除重复'''
        # 试错模式
        if (self.cut_mode == True) and (not self.cut_path == "") and (not self.cut_path == "."):
            logger.info("cut mode : true")
            for dp_list in self.duplicate_list:
                # 复制第一张图
                upper_dir = os.path.relpath(dp_list[0], self.path_in)
                full_out = os.path.normpath(os.path.join(self.path_out, upper_dir))
                dir_out = os.path.split(full_out)[0]
                if not os.path.exists(dir_out):
                    os.makedirs(dir_out)
                shutil.copy(dp_list[0], full_out)
                logger.info("copy: %s" % dp_list[0])
                # 剪切其他图
                for image in dp_list[1:]:
                    # 拼接完整输出路径
                    upper_dir = os.path.relpath(image, self.path_in)
                    full_out = os.path.normpath(os.path.join(self.path_out, upper_dir))
                    dir_out = os.path.split(full_out)[0]
                    if not os.path.exists(dir_out):
                        os.makedirs(dir_out)
                    shutil.move(image, full_out)
                    logger.info("move: %s" % image)
        # 直接删除
        else:
            logger.info("cut mode : false")
            for dp_list in self.duplicate_list:
                for image in dp_list[1:]:
                    logger.info("delete: %s" % image)
                    os.remove(image)

    def func_handle(self, methodPathIn, methodPathOut, jetzt):
        '''处理方法: 仅遍历'''
        self.image_path_list[0].append(methodPathIn)
        return "traversing"

    def run(self):
        '''开始处理'''
        logger.info("remove duplicate function start ...")
        logger.write("remove duplicate")
        if self.iter_level == "first":
            self.find_all(Traverse().get_first_file, self.func_handle)
        elif self.iter_level == "all":
            self.find_all(Traverse().get_file, self.func_handle)
        else:
            logger.error("unexpected iter_level : %s" % self.iter_level)
            return

        self.main_filter()
        self.rm_dp()
