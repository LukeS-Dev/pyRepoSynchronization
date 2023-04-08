import dotenv
import os
from datetime import datetime

SYSTEM_LOG_FILE = os.getenv("SYSTEM_LOG_FILE")

class logger: 
    def __init__(self,filename=SYSTEM_LOG_FILE, timestamp=True):
        self.filename = filename
        self.timestamp = timestamp

    def logToFile(self,message):
        content = message
        
        if self.timestamp == True:
            now = datetime.now()
            str_date_time = now.strftime("%d-%m-%Y, %H:%M:%S")
            content = str_date_time + " : " + message

        with open(self.filename,"a+") as log:
            log.write(content + "\n")

        print(content)
