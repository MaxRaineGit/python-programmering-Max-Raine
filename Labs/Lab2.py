import pandas as pd
import matplotlib.pyplot as plt

x = []
y = []

with open("Labs\\datapoints.txt", "r") as datafile:
    datapoints = pd.read_csv(datafile, delimiter=",")
    data = pd.DataFrame(datapoints)
    x_data = data['(width (cm)']
    y_data = data[' height (cm)']


plt.scatter(x_data, y_data)
plt.show()

