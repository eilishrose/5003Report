# -*- coding: utf-8 -*-
"""
Created on Mon May 17 13:42:24 2021

@author: eilish.pudney
"""

import operator
import numpy
import csv
import matplotlib 
matplotlib.use('TKAgg')
import matplotlib
import matplotlib.pyplot
import tkinter

fig = matplotlib.pyplot.figure(figsize=(7, 7))
weightedgeology = []
weightedtransport = []
weightedpopulation = []
weighteddem = []

weight1 = 0.2
weight2 = 0.3
weight3 = 0.5

# GEOLOGY

print("Geology start")

geology = numpy.array(list(csv.reader(open("geology.csv", encoding='UTF-8'), delimiter=","))).astype("int")

# print(geology)

print(geology[5][0:335])

weightedgeology = geology * weight1
print("Finished weighting Geology")
            

print(weightedgeology[5][0:335])

# POPULATION

print("Population start")


population = numpy.array(list(csv.reader(open("population.csv", encoding='UTF-8'), delimiter=","))).astype("int")

# print(population)

weightedpopulation = population * weight2
print("Finished weighting Population")

# TRANSPORT

print("Transport start")

transport = numpy.array(list(csv.reader(open("transport.csv", encoding='UTF-8'), delimiter=","))).astype("int")

# print(transport)

weightedtransport = transport * weight3
print("Finished weighting Transport")

# WEIGHTED MAP

weighteddem = numpy.add(geology, population, transport)  

# print(weighted)

# print(weighted[5][0:335])


def graph():
    
    matplotlib.pyplot.ylim(530,0)
    matplotlib.pyplot.xlim(0,335)
    matplotlib.pyplot.imshow(geology)
    matplotlib.pyplot.show()
    
def run():
    '''
    Runs the animation.
    
    Returns
    -------
    None.
    
    '''
    animation=matplotlib.animation.FuncAnimation(fig, graph, interval=1, repeat=False)

    canvas.draw()



root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


# menu_bar = tkinter.Menu(root)
# root.config(menu=menu_bar)
# model_menu = tkinter.Menu(menu_bar)
# menu_bar.add_cascade(label="Model", menu=model_menu)
# model_menu.add_command(label="Exit", command=root.destroy) #See references

# #Terminates the loop 
# def exiting(): 
#     '''
#     Terminates the loop when exiting the window

#     Returns
#     -------
#     None.

#     '''
#     root.quit()
#     root.destroy()

# root.protocol('WM_DELETE_WINDOW', exiting)

tkinter.mainloop()