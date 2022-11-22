import urllib
import json
import requests
import asyncio
import datetime
import time

from io import StringIO
class StringBuilder:
    string = None
 
    def __init__(self):
        self.string = StringIO()
 
    def Add(self, str):
        self.string.write(str)
 
    def __str__(self):
        return self.string.getvalue()


async def getALL_Data():

	while True:
		status = StringBuilder()

		response = requests.get("https://www.doviz.com/api/v5/converterItems")
		takeJson = response.json()
		status.Add("============+ "+ datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") +" +============"+"\n")
		status.Add("      Dolar: " + str(takeJson["C"]["USD"]["selling"]) + "\n")
		status.Add("       Euro: " + str(takeJson["C"]["EUR"]["selling"]) + "\n")
		status.Add("    Sterlin: " + str(takeJson["C"]["GBP"]["selling"]) + "\n")
		status.Add("Rus Rublesi: " + str(takeJson["C"]["RUB"]["selling"]) + "\n\n")
		print(status)
		time.sleep(2)
		pass

asyncio.get_event_loop().run_until_complete(getALL_Data())