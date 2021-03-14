import json
from matplotlib import pyplot as plt
from matplotlib import style  

with open("speedtest/json/download.json", "r") as downlog:
    try:
        down = json.load(downlog)
    except:
        down = {}

with open("speedtest/json/upload.json", "r") as uplog:
    try:
        up = json.load(uplog)
    except:
        up = {}

time_down = []
val_down = []
time_up = []
val_up = []

# print(down)
# print(up)

for timeval, value in down.items():
    time_down.append(timeval)
    val_down.append(value)

for timeval, value in up.items():
    time_up.append(timeval)
    val_up.append(value)

style.use('ggplot') 
plt.plot(time_down, val_down, 'cyan', label='Download', linewidth=5)    
plt.plot(time_up, val_up, 'blueviolet', label='Upload', linewidth=5)    
plt.title('Network')
plt.ylabel('Speed in MBs')    
plt.xlabel('Time')    

plt.show()