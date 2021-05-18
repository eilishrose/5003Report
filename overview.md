# 5003 Report: Site location problem

## Software intention 

Take in 3 data sets as numpy arrays
Create widgets to allow users to input variables
Use widgets to assign weighting to data 
Create a weighted dem based on the users input to the ipywidgets

## Issues during development and resolutions

### Choosing and implementing a method of getting user input variable information

Initially I worked from the provided module materials and worked to get a user interface pop up in the form of a tkinter window, however I found that the interface to be clunky. I looked into how to implement a slider within Jupyter Notebooks, and found the ipywidget package. I chose to use this package within my report as it used a small amouint of code to create the sliders, and it created an easy reference to the user input variables (.values) which is used later to create the weighting.

### Adding together three numpy arrays

### Getting code to run from the middle of the notebook

## Sources

### iPyWidgets
Button styling - https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Styling.html
IntSlider - https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html

### MatPlotLib
ColourMap styling - https://matplotlib.org/stable/gallery/color/colormap_reference.html
Adding a map title - https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.title.html

###Other

Adding in JS script to execute cells below button - https://stackoverflow.com/questions/32714783/ipython-run-all-cells-below-from-a-widget

## Software design thought process

## Software development process followed

 
