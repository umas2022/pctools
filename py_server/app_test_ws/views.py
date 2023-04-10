

from channels.generic.websocket import WebsocketConsumer


class WebsocketTest(WebsocketConsumer):
    '''websocket test'''
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
            # time.sleep(0.01)
            self.send(str(i))