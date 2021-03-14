import speedtest as st
from datetime import datetime
from time import sleep, time
import json

while True:
    try:
        s = st.Speedtest()

        ti = datetime.now()
        t = round(time())

        up = round(s.upload() * 0.000001, 2)
        down = round(s.download() * 0.000001, 2)

        print(f"{ti} - Download: {down} - Upload: {up}\n")

        with open("network.log", "a+") as log:
            log.write(f"{ti} - Download: {down:.2f} - Upload: {up:.2f}\n")

        with open("json/download.json", "r") as downlog:
            new = {t: down}

            try:
                data = json.load(downlog)
            except:
                data = {}
            data.update(new)

        with open("json/download.json", "w") as downlog:
            json.dump(data, downlog)

        with open("json/upload.json", "r") as uplog:
            new = {t: up}

            try:
                data = json.load(uplog)
            except:
                data = {}
            data.update(new)

        with open("json/upload.json", "w") as uplog:
            json.dump(data, uplog)


    except:
        time = datetime.now()

        with open("network.log", "a+") as log:
            log.write(f"{time} - Test failed\n")

    sleep(300)