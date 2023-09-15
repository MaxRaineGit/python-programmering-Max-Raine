import csv
import matplotlib.pyplot as plt

x = []
y = []

with open('datapoints.txt', "r") as datafile:
    plots = csv.reader(datafile, delimiter=',')
    for rows in plots:
        x.append(int(0))
        y.append(int(1))

plt.plot(x,y)
plt.show