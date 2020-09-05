import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import numpy
import csv
import pandas as pd

df=pd.read_csv('owid-covid-data-cleaned.csv', sep='\t', error_bad_lines=False, index_col=False, dtype='unicode')
dateCol = df['date']
usCol = df['United States']
skCol = df['South Korea']
italyCol = df['Italy']
chinaCol = df['China']

fig, ax = plt.subplots()

# x = df.date
# y = df.date

# ax.plot(x, usCol, label="United States")
# line1 = ax.plot(y, usCol, label="United States")
# line2 = ax.plot(y, skCol, label="South Korea")
# line3 = ax.plot(y, italyCol, label="Italy")
# line4 = ax.plot(y, chinaCol, label="China")

iterdata = df.iteritems()
lines = []
next(iterdata)
# for (columnName, columnData) in iterdata:
    # print('Colunm Name : ', columnName)
    # lines.append([dateCol, columnData.astype(float), columnName])
    # plt.plot(dateCol, columnData.astype(float), label=columnName)

# print(usCol[115])
    
ax.xaxis.set_major_locator(plt.MaxNLocator(5))
ax.yaxis.set_major_locator(plt.MaxNLocator(10))

# def init():
#     for line in lines:
#         line.set_data([],[])
#     return lines
x,y = [], []
# index= count()
def animate(i):
    x.append(next(i))
    y.append(usCol[i])
    plt.plot(x,y)
    # timetext.set_text(i)
    # x = numpy.array(range(1,npdata.shape[]))
    # for line in lines:
    #     # line.set_data(x:)
    #     print(line[2])

ani = FuncAnimation(fig, animate, interval=300)
# plt.xlabel('Date')
# plt.ylabel('Cases')
# plt.title('Covid 19 New Cases')
# plt.legend()
plt.show()
