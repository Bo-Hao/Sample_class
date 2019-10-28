import numpy as np 
import time
import matplotlib.pyplot as plt 
import csv
import pickle


theta = np.linspace(0, 2 * np.pi, 200)
plt.plot(200*np.cos(theta), 200*np.sin(theta), color="red", linewidth=2)
plt.show()