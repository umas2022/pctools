import sys,os
script_path =os.path.dirname(os.path.dirname(os.path.realpath(__file__))) 
sys.path.append(script_path)
from auto_trans import AutoTrans

json_set = {
    "save_path": r"D:\s-code\test\save",
    "target": "jpn_vert",
    "translate": "zh-CN"
}

mc = AutoTrans(json_set=json_set)
mc.run()
