'''
create: 忘了反正挺早的

默认frontend模式,升级win11之后在server里将mode从terminal改为frontend并不能起效
'''

from glob import glob
import os
import pkgutil
import time
import importlib
from channels.generic.websocket import WebsocketConsumer
import subprocess
import threading

from utils.stdout_catcher import *


# # 添加工具箱引用目录：backend_v2/py_script
# import sys
# server_dir = os.path.split(os.path.realpath(__file__))[0] # backend_v2/py_server
# backend_dir = os.path.split(os.path.split(server_dir)[0])[0] # backend_v2/
# script_dir = os.path.join(backend_dir,"py_script") # backend_v2/py_script
# sys.path.append(backend_dir)
# print(script_dir)
# wait=input("...")

from utils_logger.log import logger_re as logger



class SearcherBasic():
    '''SpSearcher基本方法支持'''

    def __init__(self) -> None:
        pass

    def basic_data_check(self, get_data) -> bool:
        '''检查输入参数合法性'''
        logger.debug("合法性检查(假的,这个功能还没做)")
        return True


class SearcherFunction():
    '''SpSearcher所有处理方法'''

    def __init__(self) -> None:
        pass

    def onerror(self, err):
        logger.error("SearcherFunction error : %s" % err)

    def list_update(self, get_data, send) -> None:
        '''
        更新目录
        必要参数:get_data.py_path
        '''
        logger.info("更新目录")
        index_list = {}
        group_dic = []
        index_file_path = os.path.join(get_data["py_path"], "index.json")
        index_file_data = json.load(open(index_file_path, "r", encoding="utf-8"))
        contents = os.listdir(get_data["py_path"])
        contents_path = [os.path.join(get_data["py_path"], x) for x in contents]
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
        logger.info("list update done")
        send("done")

    def get_list(self, get_data, send) -> None:
        '''
        获取目录
        必要参数: get_data.py_path
        '''
        logger.info("获取目录")
        index_file_path = os.path.join(get_data["py_path"], "index.json")
        index_file_data = json.load(open(index_file_path, "r", encoding="utf-8"))
        send(json.dumps(index_file_data))
        send("done")

    def get_intf(self, get_data, send) -> None:
        '''
        获取单个功能
        必要参数: get_data.py_path, get_data.module
        '''
        logger.info("获取单个功能")
        module_name = get_data["module"]
        intf_file_path = os.path.join(get_data["py_path"], module_name, "intf.json")
        intf_file_data = json.load(open(intf_file_path, "r", encoding="utf-8"))
        send(json.dumps(intf_file_data))
        send("done")

    def run(self, get_data, send) -> None:
        '''
        批处理函数调用
        必要参数: get_data.function, get_data.py_path, get_data.terminal, get_data.其他参数
        '''
        logger.info("get data: %s" % str(get_data))
        # 主要功能函数
        get_function = get_data["function"]
        # 由附加按钮触发的子函数
        get_button = get_data["button"] if "button" in get_data else ""

        # 定义工作主函数
        def main_func() -> None:
            logger.set_mode("frontend")
            now = time.time()

            for filefiner, name, ispkg in pkgutil.iter_modules([get_data["py_path"]]):
                if name == get_function:
                    importlib.import_module(name)
                    module = sys.modules[name]
                    mc = module.MainClass(json_set=get_data)
                    if not get_button == "":
                        called_func = getattr(mc, get_button)
                        called_func()
                    else:
                        mc.run()

            time_spent_ms = int(1000 * (time.time() - now))
            time_spent = str(time_spent_ms / 1000) + "s" if time_spent_ms > 1000 else str(time_spent_ms) + "ms"
            logger.info("time-cost: %s" % time_spent)

        # 定义日志截取函数
        def log_func(log):
            send(str(log))

        # 直接调用
        def run_direct():
            catcher = Catcher(main_func, log_func)
            catcher.run(buff_size=10)
            
        # 终端调用
        def run_terminal():
            subprocess.run(['python', './app_sp_operator/terminal_searcher.py', json.dumps(get_data)], creationflags=subprocess.CREATE_NEW_CONSOLE)
            # subprocess.run(['python', './app_sp_operator/terminal_searcher.py', json.dumps(get_data)])
        if get_data["terminal"] == True:
            go_main = threading.Thread(target=run_terminal)
            go_main.start()
            return
        go_main = threading.Thread(target=run_direct)
        go_main.start()


class SpSearcher(WebsocketConsumer):
    '''sp批处理ws函数'''

    def connect(self):
        '''ws连接'''
        self.accept()

    def disconnect(self, close_code):
        '''ws断开连接'''
        pass

    def receive(self, text_data):
        """ws接收消息"""
        logger.info("get data: %s" % str(text_data))
        get_data = json.loads(text_data)
        if not SearcherBasic().basic_data_check(get_data):
            return
        called_func = getattr(SearcherFunction(), get_data["function"])
        called_func(get_data["data"], self.send)
