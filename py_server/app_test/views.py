import subprocess
from django.http import HttpResponse
import time
from channels.generic.websocket import WebsocketConsumer
import json
import os


def app_test(request):
    '''basic response test'''
    print("request:")
    print(request.body)
    return HttpResponse("test Hello world ")


class AppTestWS(WebsocketConsumer):
    '''test类'''

    def __init__(self) -> None:
        super().__init__()
        self.data = {}

    def connect(self):
        '''ws连接'''
        self.accept()

    def disconnect(self, close_code) -> None:
        '''ws断开'''
        pass

    def receive(self, text_data) -> None:
        '''ws接收'''
        json_data = json.loads(text_data)

        time_start = time.time()


        subprocess.run(['python3', './app_test/call_terminal.py','arg1','arg2','arg3','arg4'],
                        creationflags=subprocess.CREATE_NEW_CONSOLE)

