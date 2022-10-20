import time
from channels.generic.websocket import WebsocketConsumer
import subprocess
import threading

from utils.stdout_catcher import *
from py_script.sp_manager import SpManager
from py_script.sp_manager import logger


class SpOperator(WebsocketConsumer):
    '''sp批处理程序中间件'''

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
            subprocess.run(['python3', './app_sp_operator/call_terminal.py', json.dumps(get_data)], creationflags=subprocess.CREATE_NEW_CONSOLE)
            # subprocess.run(['python3', './app_sp_operator/call_terminal.py', json.dumps(get_data)])
        if "terminal" in get_data:
            go_main = threading.Thread(target=run_terminal)
            go_main.start()
        else:
            go_main = threading.Thread(target=run_direct)
            go_main.start()
