import matplotlib
import matplotlib.pyplot
import csv
import matplotlib.animation

environment =[]

# Import raster data set and append data to list
f = open('snow.csv', newline='' )
reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
for row in reader: 
    rowlist = []
    environment.append(rowlist)
    for value in row:
        rowlist.append(value)
        print(value)
f.close()

#Plot the agents
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
