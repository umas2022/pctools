

import sys, os

script_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(script_path)
from sp_remove_keyword.remove_keyword import RemoveKeyword as MainClass



json_set = {
    'path_in': r'D:\s-samu\Tama作品更新补全',
    'keyword' : "_1.",
    # "location":"-1",
    # "path_log": "",
}

vc = MainClass(json_set)
vc.run()

