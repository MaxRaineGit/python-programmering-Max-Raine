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
        all_training.append({'width': width, 'height': height, 'label': label})
        if label == 0:
            pichu_training.append({'width': width, 'height': height, 'label': label})
        if label == 1:
            pikachu_training.append({'width': width, 'height': height, 'label': label}) 


pichu_x = [point['width'] for point in pichu_training]
pichu_y = [point['height'] for point in pichu_training]
pikachu_x = [point['width'] for point in pikachu_training]
pikachu_y = [point['height'] for point in pikachu_training]

plt.scatter(pichu_x, pichu_y, color='red', label='Pichu')
plt.scatter(pikachu_x, pikachu_y, color='blue', label='Pikachu')
plt.legend()
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
        label = "Pichu"
    else:
        label = "Pikachu"

    return label


testpoints = []

with open("Labs\\testpoints.txt", 'r') as testfile:
    testdata = testfile.readlines()
    for line in testdata:
        if '(' not in line:
            continue
        # using map to convert the string to float and creating the variables "width" and "Height" while also trimming down testpoints.txt so i can extract them correctly and asign them to the newly created variables.
        width, height = map(float, line.strip().split('(')[1].split(')')[0].split(','))
        testpoints.append({'width': width, 'height': height})

for testpoints in testpoints:
    testpoints_label = find_closest_points(testpoints, all_training)
    print(f"{testpoints} is a {testpoints_label}!")

try:
    user_width = float(input("Enter the width: "))
    user_height = float(input("Enter the height: "))

    user_point = {'width': user_width, 'height': user_height}
    user_point_label = find_closest_points(user_point, all_training)
    print(f"{user_point} is a {user_point_label}")

except ValueError:
    print("Please only use numeric values for width and height, Please try again")