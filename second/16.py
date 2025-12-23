'''Q16. Write a Python program to draw a sine wave (y = sin(x)).
Program:'''
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10, 400)
y = np.sin(x)
plt.plot(x, y)
plt.grid(True)
plt.show()