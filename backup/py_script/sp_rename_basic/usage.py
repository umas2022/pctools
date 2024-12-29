import sys,os
script_path =os.path.dirname(os.path.dirname(os.path.realpath(__file__))) 
sys.path.append(script_path)
from sp_rename_basic.rename_basic import RenameBasic as MainClass


'''
添加前缀    add_prefix
删除前缀    del_prefix
关键字替换  replace_key
序号命名    num_array
'''

path_in = r'D:\s-code\test\test_out'
json_set = {
    "path_in": r"C:\Users\umas2\Downloads\新建文件夹\gweda 2024.11.02\202410",
    "use_func": "add_prefix",
    "target": "dir",
    "add_in": "2024-10-",
    "add_in_2": "",
    "deep":False
}

vc = MainClass(json_set=json_set)
vc.run()
