from glob import glob
import os
import pkgutil
import time
import importlib
from channels.generic.websocket import WebsocketConsumer
import subprocess
import threading

from utils.stdout_catcher import *
from py_script.sp_manager import SpManager
from py_script.sp_manager import logger


class SpOperator(WebsocketConsumer):
    '''
    sp批处理程序中间函数
    调用sp_manager.py
    已被直接搜索py_script目录的方法替代
    '''

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        """
        接收消息
        :param text_data: 客户端发送的消息
        :return:
        """
        logger.info("get data: %s" % str(text_data))
        get_data = json.loads(text_data)
        get_function = get_data["function"]

        # 定义工作主函数
        def main_func() -> None:
            logger.set_mode("frontend")
            sm = SpManager()
            if not get_function in dir(sm):
                logger.error("sp-manager: unexpected function - %s" % get_function)
                return
            now = time.process_time()
            called_func = getattr(sm, get_function)
            called_func(json_set=get_data)
            time_spent_ms = int(1000 * (time.process_time() - now))
            time_spent = str(time_spent_ms / 1000) + "s" if time_spent_ms > 1000 else str(time_spent_ms) + "ms"
            logger.info("time-spent: %s" % time_spent)

        # 定义日志截取函数
        def log_func(log):
            self.send(str(log))

        # 直接调用
        def run_direct():
            catcher = Catcher(main_func, log_func)
            catcher.run(buff_size=10)
        # 终端调用

        def run_terminal():
            subprocess.run(['python3', './app_sp_operator/terminal_operator.py', json.dumps(get_data)], creationflags=subprocess.CREATE_NEW_CONSOLE)
            # subprocess.run(['python3', './app_sp_operator/terminal_operator.py', json.dumps(get_data)])
        if "terminal" in get_data:
            if get_data["terminal"] == True:
                go_main = threading.Thread(target=run_terminal)
                go_main.start()
                return
        go_main = threading.Thread(target=run_direct)
        go_main.start()


class SearcherBasic():
    '''SpSearcher基本方法支持'''

    def __init__(self) -> None:
        pass

    def basic_data_check(self, get_data) -> bool:
        '''检查输入参数合法性'''
        logger.debug("输入参数合法性检查还没做")
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
        index_list = []
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
                    key = contents[contents_path.index(item)]
                    index_list.append({"title": intf_json["title"], "key": key})
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

    def get_intf(self,get_data,send)->None:
        '''
        获取单个功能
        必要参数: get_data.py_path, get_data.module
        '''
        logger.info("获取单个功能")
        module_name = get_data["module"]
        intf_file_path = os.path.join(get_data["py_path"],module_name, "intf.json")
        intf_file_data = json.load(open(intf_file_path, "r", encoding="utf-8"))
        send(json.dumps(intf_file_data))
        send("done")

    def run(self,get_data,send)->None:
        '''
        批处理函数调用
        必要参数: get_data.function, get_data.py_path, get_data.terminal, get_data.其他参数
        '''
        logger.info("get data: %s" % str(get_data))
        get_function = get_data["function"]

        # 定义工作主函数
        def main_func() -> None:
            logger.set_mode("frontend")
            now = time.process_time()

            for filefiner,name,ispkg in pkgutil.iter_modules([get_data["py_path"]]):
                if name == get_data["function"]:
                    importlib.import_module(name)
                    module = sys.modules[name]
                    mc = module.MainClass(json_set = get_data)
                    mc.run()
            
            time_spent_ms = int(1000 * (time.process_time() - now))
            time_spent = str(time_spent_ms / 1000) + "s" if time_spent_ms > 1000 else str(time_spent_ms) + "ms"
            logger.info("time-spent: %s" % time_spent)

        # 定义日志截取函数
        def log_func(log):
            send(str(log))

        # 直接调用
        def run_direct():
            catcher = Catcher(main_func, log_func)
            catcher.run(buff_size=10)
        # 终端调用
        def run_terminal():
            subprocess.run(['python3', './app_sp_operator/terminal_searcher.py', json.dumps(get_data)], creationflags=subprocess.CREATE_NEW_CONSOLE)
            # subprocess.run(['python3', './app_sp_operator/terminal_searcher.py', json.dumps(get_data)])
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
