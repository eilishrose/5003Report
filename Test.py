import matplotlib
import matplotlib.pyplot
import csv
    
snowslope =[]

# Import raster data set and append data to list
f = open('snowslope.csv', newline='' )
reader = csv.reader(f,  delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
for row in reader: 
    rowlist = []
    snowslope.append(rowlist)
    for value in row:
        rowlist.append(value)
       # print(value)
f.close()

num_of_columns = len(row)
print(num_of_columns)


#for i in range: 
    
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(snowslope)
