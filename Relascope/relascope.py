import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse
import math 
import pickle
 

'''def rtpy(x, theta, D):
    t = x**2*(1+math.tan(theta)**2/1600)
    y = 2500 - D*math.tan(theta) - t
    return y**0.5
def rtny(x, theta, D):
    t = x**2*(1+math.tan(theta)**2/1600)
    y = 2500 - D*math.tan(theta) - t
    return -y**0.5

def cal_xlim(theta, D):
    x = (50**2 - D*math.tan(theta))/(1+math.tan(theta)**2/1600)
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
'''

def find_gamma_(Distance, height_of_tree, radius_of_tree, elevation):
    # simplify the symbols 
    D = Distance
    e = elevation # radian
    h = height_of_tree
    r = radius_of_tree
    

    # l and lr
    x1 = (D * math.tan(e) - h) / (math.tan(e) - h / r)
    z1 = -h / r * (x1 - r)
    
    # l and ll
    x2 = (D * math.tan(e) - h) / (math.tan(e) + h / r)
    z2 = h / r * (x2 + r)

    
    a = 0.5 * ((x1 - x2)**2 + (z1 - z2)**2)**0.5
    b = r - r * D * np.tan(e) / h

    x0 = a**2 * math.cos(e) / D
    y0 = b**2 - a**2 * b**2 * math.cos(e)**2 / D**2
    y0 = y0**0.5 if y0 >= 0 else (-y0)**0.5

    m1 = b**2 * x0 / a**2 / y0
    

    af = (a**2  * b **2 * D**2 / math.cos(e)**2 - a**4 * b**2)
    cf = -a**4 * b**2

    m2 = (-4 * af * cf)**0.5 / 2 / af
    #print(m1, m2)

    gamma = 2 * math.atan(m1)

    return gamma
 
def critical_height(gamma, Distance, height_of_tree, radius_of_tree):
    
    D = Distance
    h = height_of_tree
    r = radius_of_tree
    
    rc = D * np.sin(gamma/2)
    Z = h * (r - rc) / r 
    
    return Z

def elevation_calibate(gamma, Distance, height_of_tree, radius_of_tree):
   
    D = Distance
    h = height_of_tree
    r = radius_of_tree

    rc = D * math.sin(gamma/2)
    Zc = h * (r - rc) / r 

    xc = rc * math.cos(np.pi / 2 - gamma / 2)
    a = Zc / (D - xc)

    new_elevation = math.atan(a)

    return new_elevation

def calibrate(angle, elevation):
    # a: angle e: elevation
    a = angle
    e = elevation
    new_angle = math.acos(math.sin(e)**2 + math.cos(a) * math.cos(e)**2)
    return new_angle

def main():
    bafs = [[1, 9], [1, 37], [1, 59], [2, 18], [2, 34], [2, 48]]
    new_bafs = [(i[0]+i[1]/60)/180*np.pi for i in bafs]

    Distance = 1000
    height_of_tree = 2000
    radius_of_tree = 25 

    data = [[], [], []]
    for BAF in new_bafs:
        criti_height = critical_height(BAF, Distance, height_of_tree, radius_of_tree)
        
        new_elevation = elevation_calibate(BAF, Distance, height_of_tree, radius_of_tree)
        
        elevation = math.atan(criti_height / Distance)
        
        
        the_angle = find_gamma_(Distance, height_of_tree, radius_of_tree, new_elevation)
        
        rela_angle = calibrate(BAF, new_elevation)

        print( the_angle/np.pi*180,  rela_angle/np.pi*180)
        


main()
