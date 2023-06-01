
import sys,os
script_path =os.path.dirname(os.path.dirname(os.path.realpath(__file__))) 
sys.path.append(script_path)

from sp_copy_merge.copy_merge import CopyMerge


# path_in = r'D:\s-code\test\test_in'
# path_out = r'D:\s-code\test\test_out'
path_in = r"C:\Users\umas-vt\samu-vt\wfs\#ww\そらなにいろ2023.04.22\そらなにいろ@お仕事募集中"
path_out = r"C:\Users\umas-vt\samu-vt\wfs\#ww\そらなにいろ2023.04.22\そらなにいろ@お仕事募集中2"

vc = CopyMerge(path_in,path_out)
vc.run()