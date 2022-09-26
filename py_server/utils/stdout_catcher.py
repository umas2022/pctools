'''截取系统输出'''

'''用例：

def print_test():
    print("a")
    time.sleep(1)
    print("b")
    time.sleep(1)
    print("c")


logget = []
def callback(log):
    global logget
    logget.append(log)
    logget.append(time.time())


catcher = Catcher(print_test, callback)
catcher.run()
print(logget)

'''

import sys
import time
import threading
import json


class TextArea:
    '''
    替换stdout(启动替换后回调函数中不能使用print)\n
    消息以数组形式打包发送，防止消息阻塞
    '''

    def __init__(self, catch_func, buff_size=0, buff_time=0.5) -> None:
        '''buff_size = 0 ; 默认不使用缓存包'''
        # 捕获函数
        self.catch_func = catch_func
        # 缓存容量
        self.buff_size = buff_size
        # 缓存时间
        self.buff_time = buff_time
        # 缓存
        self.buffer = []
        # 延时发送线程
        self.timer = threading.Timer(self.buff_time,self.send_buffer)

    def send_buffer(self):
        self.catch_func(json.dumps(self.buffer))
        self.buffer = []

    def buffer_add(self, msg):
        '''打包发送'''
        self.buffer.append(msg)
        self.timer.cancel()
        # buffer存满发送
        if len(self.buffer) == self.buff_size:
            self.catch_func(json.dumps(self.buffer))
            self.buffer = []
        # 到达时限发送
        else:
            self.timer = threading.Timer(self.buff_time,self.send_buffer)
            self.timer.start()

    def write(self, *args, **kwargs):
        '''重写输出函数'''
        # 无缓存直接发送
        if self.buff_size == 0:
            if args[0] != '\n':
                self.catch_func(str(args[0]))
        # 有缓存存入buffer
        else:
            if args[0] != '\n':
                self.buffer_add(str(args[0]))


class Catcher:
    '''
    封装重定向函数\n
    main_func: 被截获的函数\n
    catch_func: 截获内容的处理函数
    '''

    def __init__(self, main_func, catch_func) -> None:
        self.main_func = main_func
        self.catch_func = catch_func

    def run(self, buff_size=0):
        '''设置buff_size以启用打包模式'''
        # 重定向系统输出
        stdout = sys.stdout
        sys.stdout = TextArea(self.catch_func, buff_size)
        # 运行主函数
        self.main_func()
        # 截获系统输出
        text_area = sys.stdout
        # 恢复系统输出，不然后面不能再print了
        sys.stdout = stdout
