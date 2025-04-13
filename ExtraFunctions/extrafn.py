import matplotlib.pyplot as plt 
import numpy as np    


# snippet copied from https://stackoverflow.com/questions/7941226/how-to-add-line-based-on-slope-and-intercept answered by ak_slick and David Marx 
def line_with_slope_and_intercept(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')

