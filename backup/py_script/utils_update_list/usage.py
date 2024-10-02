import sys,os
script_path =os.path.dirname(os.path.dirname(os.path.realpath(__file__))) 
sys.path.append(script_path)

from utils_update_list.update import list_update


list_update(script_path)