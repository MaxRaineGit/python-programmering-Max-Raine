
import matplotlib.pyplot as plt
import csv


##with open("Labs\\datapoints.csv", "r") as datafile:
 #   datapoints = pd.read_csv(datafile, delimiter=",")
 #   data = pd.DataFrame(datapoints)
 #   x_data = data['(width (cm)']
  #  y_data = data[' height (cm)']
    
##data = data.drop(' 1-pikachu))', axis=1)
#data = data.rename(columns={"(width (cm)": "Width", " height (cm)": "Height", " label (0-pichu": "Class"})

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

    #for row in data:
        #training.append({"Width": row["(width (cm)"], "Height": row[" height (cm)"], "Class": row[" label (0-pichu"]})



plt.scatter([x[0] for x in pichu_training], [y[1]for y in pichu_training], color = 'red')
plt.scatter([x[0] for x in pikachu_training], [y[1]for y in pikachu_training], color = 'blue')
plt.show()


