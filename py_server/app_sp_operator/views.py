from channels.generic.websocket import WebsocketConsumer

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

        for i in range(1000):
            print(i)
            self.send(str(i))