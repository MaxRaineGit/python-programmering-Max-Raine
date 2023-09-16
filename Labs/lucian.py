import csv
import matplotlib.pyplot as plt

#x = []
#y = []

with open("Labs\\datapoints.txt", "r") as datafile:
    plots = csv.reader(datafile)

print(plots)