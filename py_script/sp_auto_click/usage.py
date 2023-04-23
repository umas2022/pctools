import sys,os
script_path =os.path.dirname(os.path.dirname(os.path.realpath(__file__))) 
sys.path.append(script_path)
from sp_auto_click.auto_click import AutoClick as MainClass


json_set = {
    'pos_x': '100',
    'pos_y': '100',
    'sleep_time': "1",
}
  
mc = MainClass(json_set)
# mc.run()
mc.get_pos()   