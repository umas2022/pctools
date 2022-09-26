import time
from channels.generic.websocket import WebsocketConsumer

from utils.stdout_catcher import *


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
        print(text_data)

        # 定义工作主函数
        def main_func() -> None:
            now = time.process_time()
            for i in range(10000):
                print(i)
            print("py-time: %s ms" % str(int(1000 * (time.process_time() - now))))

        # 定义日志截取函数
        def log_func(log):
            self.send(str(log))

        # 调用
        catcher = Catcher(main_func, log_func)
        catcher.run(buff_size=10)
        # catcher.run()
