import math
import matplotlib.pyplot as plt
import csv


pichu_training = []
pikachu_training = []

with open("Labs\\datapoints.txt", "r") as file:
    data = csv.reader(file, delimiter=",")
    next(data, None)
    for row in data:
        width, height, label = map(float, row)
        if label == 0:
            pichu_training.append([width, height])
        if label == 1:
            pikachu_training.append([width, height])

   



plt.scatter([x[0] for x in pichu_training], [y[1]for y in pichu_training], color = 'red')
plt.scatter([x[0] for x in pikachu_training], [y[1]for y in pikachu_training], color = 'blue')
plt.show()

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
