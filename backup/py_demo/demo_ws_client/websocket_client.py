'''
2022.12.5
websocket简易客户端,验证后端ws服务器
'''
from websocket import create_connection

ws = create_connection("ws://localhost:8008/demo_websocket")
#print(ws.recv())
print("Sending 'Hello, World'...")
ws.send("Hello, World")
while True:
	result =  ws.recv()
	print("Received '%s'" % result)
ws.close()

