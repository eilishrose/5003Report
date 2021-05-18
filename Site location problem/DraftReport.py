# -*- coding: utf-8 -*-
"""
Created on Sun May 16 22:24:16 2021

@author: George
"""

import csv
import matplotlib
import matplotlib.pyplot
import tkinter
matplotlib.use('TkAgg')

weight1 = 0.2
weight2 = 0.3
weight3 = 0.5

weightedgeology = []
weightedtransport = []
weightedpopulation = []

# IMPORT AND SHOW GEOLOGY

f = open('geology.csv', newline='' )
geology = []
reader = csv.reader(f,  delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
for row in reader: 
    rowlist = []
    geology.append(rowlist)
    for value in row:
        rowlist.append(value)
f.close()

#JUPYTER
# matplotlib.pyplot.ylim(530,0)
# matplotlib.pyplot.xlim(0,335)
# matplotlib.pyplot.imshow(geology)

# IMPORT AND SHOW TRANSPORT

f = open('transport.csv', newline='' )
transport = []
reader = csv.reader(f,  delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
for row in reader: 
    rowlist = []
    transport.append(rowlist)
    for value in row:
        rowlist.append(value)
f.close()

# matplotlib.pyplot.ylim(530,0)
# matplotlib.pyplot.xlim(0,335)
# matplotlib.pyplot.imshow(transport)

# IMPORT AND SHOW POPULATION

f = open('population.csv', newline='' )
population = []
reader = csv.reader(f,  delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
for row in reader: 
    rowlist = []
    population.append(rowlist)
    for value in row:
        rowlist.append(value)
f.close()

# matplotlib.pyplot.ylim(530,0)
# matplotlib.pyplot.xlim(0,335)
# matplotlib.pyplot.imshow(population)

# print(geology[5][0:335])

for i in geology: 
    weightedgeology = []   
    for row in geology:       
        rowlist = []       
        weightedgeology.append(rowlist)       
        for value in row:           
            rowlist.append(weight1 * value)
            
# print(weightedgeology[5][0:335])

# print(transport[5][0:335])

for i in transport: 
    weightedtransport = []   
    for row in transport:       
        rowlist = []       
        weightedtransport.append(rowlist)       
        for value in row:           
            rowlist.append(weight2 * value)

# print(weightedtransport[5][0:335])

# print(population[5][0:335])

for i in population: 
    weightedpopulation = []   
    for row in population:       
        rowlist = []       
        weightedpopulation.append(rowlist)       
        for value in row:           
            rowlist.append(weight3 * value)

# print(weightedpopulation[5][0:335])

# fig = matplotlib.pyplot.figure(figsize=(7, 7))
# ax = fig.add_axes([0, 0, 1, 1])

# root = tkinter.Tk()
# root.wm_title("Model")
# canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
# canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)