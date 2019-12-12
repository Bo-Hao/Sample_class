import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse
 

def rtpy(x, theta, D):
    t = x**2*(1+np.tan(theta)**2/1600)
    y = 2500 - D*np.tan(theta) - t
    return y**0.5
def rtny(x, theta, D):
    t = x**2*(1+np.tan(theta)**2/1600)
    y = 2500 - D*np.tan(theta) - t
    return -y**0.5

def cal_xlim(theta, D):
    x = (50**2 - D*np.tan(theta))/(1+np.tan(theta)**2/1600)
    return x**0.5

D = 1000

for degree in [30, 45, 60]:
    #degree = 89
    theta = degree/180*np.pi

    lim = cal_xlim(theta, D)
    x = np.linspace(-lim, lim, 100)

    plt.scatter(x, rtpy(x, theta, D))
    plt.scatter(x, rtny(x, theta, D))

plt.show()
