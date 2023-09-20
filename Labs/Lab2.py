import math
import matplotlib.pyplot as plt
import csv


pichu_training = []
pikachu_training = []
all_training = []

with open("Labs\\datapoints.txt", "r") as file:
    data = csv.reader(file, delimiter=",")
    next(data, None)
    for row in data:
        width, height, label = map(float, row)
        all_training.append([width, height, label])
        if label == 0:
            pichu_training.append([width, height, label])
        if label == 1:
            pikachu_training.append([width, height, label])  


plt.scatter([x[0] for x in pichu_training], [y[1]for y in pichu_training], color = 'red')
plt.scatter([x[0] for x in pikachu_training], [y[1]for y in pikachu_training], color = 'blue')
plt.show()


def distance(point1, point2):
    return math.sqrt((point1['width'] - point2['width'])**2 + (point1['height'] - point2['height'])**2)

def find_closest_points(new_point, all_points):
    # Calculates the disctance 📐
    distances = [(point, distance(new_point, point)) for point in all_points]

    # Sorted through the list of distances by distance.
    # Lambda is used to have a smaller function just to sort this without having to define another full function.
    sorted_distances = sorted(distances, key=lambda x: x[1])

    # Selected the 10 closest
    closest_points = [point for point, i in sorted_distances[:10]]

    # Counts the labels on the points
    pichu = sum(1 for point in closest_points if point['label'] == 0)
    pikachu = sum(1 for point in closest_points if point['label'] == 1)

    # Determines if new point is pichu or pikachu and asigns them that label
    if pichu > pikachu:
        label = 0
    else:
        label = 1

    return label
