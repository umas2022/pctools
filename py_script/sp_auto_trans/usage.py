import sys,os
script_path =os.path.dirname(os.path.dirname(os.path.realpath(__file__))) 
sys.path.append(script_path)
from sp_auto_trans import MainClass

json_set = {
    "save_path": r"D:\s-code\test\save",
    "target": "jpn_vert",
    "translate": "zh-CN"
}

mc = MainClass(json_set=json_set)
mc.run()
