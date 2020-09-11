import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import random
import numpy as np
import csv
import pandas as pd

df=pd.read_csv('owid-covid-data-cleaned.csv', sep='\t', error_bad_lines=False, index_col=False, dtype='unicode')
dateCol = df['date']

# class LinePlot:
#     def __init__(self, data):
#         self.data = data

#     # test = 'successful thangz'

#     def f(self):
#         return self.data

# covidPlot = LinePlot(df)

# print(covidPlot.f())

# def get_xticks():

xticks = []
intervals = np.linspace(0, len(dateCol) -1, num=6)
xticks = [dateCol[math.floor(interval)] for interval in intervals]

fig, ax = plt.subplots(sharex=True, sharey=True)
ax.set_xlim(0.0, 5)
ax.set_xticklabels(xticks)
xdata = []
lines, data = {}, {}
colors = ["b", "g", "r", "c", "m"]
iterdata = df.iteritems()
next(iterdata)
item = 0
for (columnName, columnData) in iterdata:
    # print('Colunm Name : ', item)
    key = "ln"+ str(item)
    lines[key], = plt.plot([], [], colors[item], animated=True, label=columnName)
    data[key] = []
    item+=1

f = np.linspace(0, len(dateCol)+1, len(dateCol)+1)

def init():
    ax.set_ylim(0, 81000)
    return lines["ln0"], lines["ln1"], lines["ln2"], lines["ln3"],

count = 0
def update(i):
    global count, lines, data
    ax.set_xlim(0.0, len(dateCol))
    xdata.append(i)
    item = 0
    iterdata = df.iteritems()
    if(count < len(dateCol) - 1):
        next(iterdata)
        for (columnName, columnData) in iterdata:
            key = "ln" + str(item)
            data[key].append(float(columnData[count]))
            lines[key].set_data(xdata, data[key])
            item+=1

        count+=1
    
    return lines["ln0"], lines["ln1"], lines["ln2"], lines["ln3"],


# ax.plot(x, usCol, label="United States")
# line1 = ax.plot(y, usCol, label="United States")
# line2 = ax.plot(y, skCol, label="South Korea")
# line3 = ax.plot(y, italyCol, label="Italy")
# line4 = ax.plot(y, chinaCol, label="China")



ani = FuncAnimation(fig, update, frames=f,
                    init_func=init, blit=True, interval=10,repeat=False)

ani.save('animated-covid-data.mp4')

# plt.tight_layout()
plt.xlabel('Date')
plt.ylabel('Cases')
plt.title('Covid 19 New Cases')
plt.legend()
plt.show()
