import numpy as np 
import time
import matplotlib.pyplot as plt 




def benefit(n, p):
    return p*n



ran = np.arange(0.7, 1.3, 0.01)
for p in ran:
    for n in ran:
        earn = benefit(n, p)
        
        if earn > 1.01:
            plt.scatter(n, p, c = 'blue', s = earn**3)
        elif earn < 0.99:
            plt.scatter(n, p, c = 'red', s = 1/earn**3)
        else:

            plt.scatter(n, p, c = "green", s = earn**3)



plt.title("Profit and Loss")
plt.xlabel('difference of number')
plt.ylabel('difference of price')
plt.show()
