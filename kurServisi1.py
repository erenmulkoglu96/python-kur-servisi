import datetime
import asyncio
import time
from json import loads
from pprint import pprint

import websockets
from websockets.legacy.client import WebSocketClientProtocol

from io import StringIO
class StringBuilder:
    string = None
 
    def __init__(self):
        self.string = StringIO()
 
    def Add(self, str):
        self.string.write(str)
 
    def __str__(self):
        return self.string.getvalue()

WS_ADRESS = "wss://socket2.paratic.com/socket.io/?EIO=4&transport=websocket"
WS_USD_TRY_MESSAGE = r'42["joinStream", {"codes": ["USD/TRL"]}]'  # Dolar
WS_EUR_TRY_MESSAGE = r'42["joinStream", {"codes": ["EUR/TRL"]}]'  # Euro
WS_GBP_TRY_MESSAGE = r'42["joinStream", {"codes": ["GBP/TRL"]}]'  # Sterlin
WS_RUB_TRY_MESSAGE = r'42["joinStream", {"codes": ["RUB/TRL"]}]'  # Rus Rublesi
WS_SEK_TRY_MESSAGE = r'42["joinStream", {"codes": ["SEK/TRL"]}]'  # İsveç Kronu


async def main():    

    async with websockets.connect(WS_ADRESS) as ws:
        ws: WebSocketClientProtocol

        await ws.recv()
        await ws.send("40")

        await ws.recv()
        await ws.recv()
        await ws.recv()

        while True:
            sb = StringBuilder()
            sb.Add("============+ " + datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S") + " +============\n")    

            await ws.send(WS_USD_TRY_MESSAGE)# Dolar
            data = str(await ws.recv())
            if "spot_pariteler" in data:
                price = data.split("|")[2]
                sb.Add("      Dolar: " + price + "₺\n")
                await ws.send("3")

            await ws.send(WS_EUR_TRY_MESSAGE)# Euro
            data = str(await ws.recv())
            if "spot_pariteler" in data:
                price = data.split("|")[2]
                sb.Add("       Euro: " + price + "₺\n")
                await ws.send("3")

            await ws.send(WS_GBP_TRY_MESSAGE)# Sterlin
            data = str(await ws.recv())
            if "spot_pariteler" in data:
                price = data.split("|")[2]
                sb.Add("    Sterlin: " + price + "₺\n")
                await ws.send("3")

            await ws.send(WS_SEK_TRY_MESSAGE)# İsveç Kronu
            data = str(await ws.recv())
            if "spot_pariteler" in data:
                price = data.split("|")[2]
                sb.Add("İsveç Kronu: " + price + "₺\n")
                await ws.send("3")

            await ws.send(WS_RUB_TRY_MESSAGE)# Rus Rublesi
            data = str(await ws.recv())
            if "spot_pariteler" in data:
                price = data.split("|")[2]
                sb.Add("Rus Rublesi: " + price + "₺\n")
                await ws.send("3")

            print(sb)
            pass        

asyncio.get_event_loop().run_until_complete(main())