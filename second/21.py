'''Q21. Write a Python program to plot a cosine wave (y = cos(x)).'''
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10, 400)
y = np.cos(x)
plt.plot(x, y)
plt.grid(True)
plt.show()