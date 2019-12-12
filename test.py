
import numpy as np 
from math import * 
import matplotlib.pyplot as plt

def f(a, e):
    # a: angle e: elevation
    a = a/180*np.pi
    e = e/180*np.pi
    new_angle = acos(np.sin(e)**2 + np.cos(a) * np.cos(e)**2)
    return 0.5*new_angle*180/np.pi


#bafs = [[1, 9], [1, 37], [1, 59], [2, 18], [2, 34], [2, 48]]


bafs = [asin(sqrt(i/2500)/2)*2/np.pi*180 for i in np.arange(1, 11, 1)]




color = ['red', 'blue', 'green', 'black', 'gray', 'red', 'blue', 'green', 'black', 'gray']

for baf in range(len(bafs)):
    for j in np.arange(0, 90, 0.5):
        plt.scatter(f(bafs[baf], j), j, c = color[baf], s= 0.5)
        plt.scatter(f(bafs[baf], j), -j, c = color[baf], s= 0.5)
        plt.scatter(-f(bafs[baf], j), j, c = color[baf], s= 0.5)
        plt.scatter(-f(bafs[baf], j), -j, c = color[baf], s= 0.5)

plt.show()