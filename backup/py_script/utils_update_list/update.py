'''
2023.4.19
更新目录index.json
'''

import os
import json


def list_update(script_path) -> None:
    '''
    更新目录
    必要参数:py_script脚本所在路径
    '''
    index_list = {}
    group_dic = []
    index_file_path = os.path.normpath(os.path.join(script_path, "index.json"))
    index_file_data = json.load(open(index_file_path, "r", encoding="utf-8"))
    contents = os.listdir(script_path)
    contents_path = [os.path.join(script_path, x) for x in contents]
    # 遍历搜索具有intf.json的文件夹
    for item in contents_path:
        if os.path.isdir(item):
            intf_path = os.path.join(item, "intf.json")
            if os.path.isfile(intf_path):
                intf_json = json.load(open(intf_path, "r", encoding="utf-8"))
                func_key = contents[contents_path.index(item)]

                group = intf_json["group"]["key"]
                group_label = intf_json["group"]["label"]
                if not group in group_dic:
                    index_list[group] = {"label": group_label, "data": {}}
                    group_dic.append(group)
                index_list[group]["data"][func_key] = intf_json["title"]

    index_file_data["data"] = index_list
    # 写入index.json
    with open(index_file_path, "w", encoding="utf-8") as index_file:
        index_file.write(json.dumps(index_file_data, ensure_ascii=False) + "\n")
