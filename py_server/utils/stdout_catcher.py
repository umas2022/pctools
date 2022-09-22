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


class TextArea:
    '''替换stdout，回调函数中不能再使用print'''
    def __init__(self, catch_func) -> None:
        # self.buffer = []
        self.catch_func = catch_func

    def write(self, *args, **kwargs):
        if args[0]!='\n':
            self.catch_func(str(args[0]))
        # self.buffer.append(args)


class Catcher:
    '''封装重定向函数'''
    def __init__(self, log_func, catch_func) -> None:
        self.log_func = log_func
        self.catch_func = catch_func

    def run(self):
        stdout = sys.stdout
        sys.stdout = TextArea(self.catch_func)  # 重定向系统输出

        self.log_func()

        text_area = sys.stdout  # 截获系统输出
        sys.stdout = stdout  # 恢复系统输出，不然后面不能再print了

        # print(text_area.buffer)


