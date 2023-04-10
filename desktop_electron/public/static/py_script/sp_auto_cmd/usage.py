import sys
sys.path.append("..")
from sp_auto_static import MainClass



json_set = {
    "path_cash": "D:\\s-code\\test\\cash",
    "win_name":"碧蓝航线",
    "interval_time":1
}

qs = MainClass(json_set=json_set)
qs.run()
