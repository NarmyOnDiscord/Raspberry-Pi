import speedtest as st
from datetime import datetime as dt
from time import sleep as wait


while True:
    try:
        s = st.Speedtest()

        time = dt.now()

        up = round(s.upload() * 0.000001, 2)
        down = round(s.download() * 0.000001, 2)

        print(f"{time} - Download: {down} - Upload: {up}\n")

        with open("network.log", "a+") as log:
            log.write(f"{time} - Download: {down} - Upload: {up}\n")

    except:
        time = dt.utcnow()

        with open("network.log", "a+") as log:
            log.write(f"{time} - Test failed\n")

    wait(60)