'''
create: 2023.2.17
utils的测试
'''

import os
import sys
py_path = os.path.split(os.path.realpath(__file__))[0]
script_path = os.path.split(py_path)[0]
sys.path.append(script_path)
from utils_tools.string_tools import StringTools


keyword = ".txt"
template = "file.txt"
location = -1
res = StringTools().location_match(template=template,keyword=keyword,location=location)
print(res)
