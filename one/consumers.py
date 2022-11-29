import time
from channels.generic.websocket import WebsocketConsumer
from one.bussiness import Domain

class OneConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        D = Domain()
        for i in range(100):
            data = D.do()
            self.send(data)
            time.sleep(2)