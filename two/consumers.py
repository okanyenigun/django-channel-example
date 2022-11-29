import time
from channels.generic.websocket import AsyncWebsocketConsumer
from asyncio import sleep
from two.business import DomainTwo

class TwoConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        D = DomainTwo()
        for i in range(100):
            data = D.do()
            await self.send(data)
            await sleep(2)