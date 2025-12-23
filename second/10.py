'''Q10. Write a Python program to draw a pentagon.
Program:'''
import matplotlib.pyplot as plt
import numpy as np
angles = np.linspace(0, 2*np.pi, 6)
x = np.cos(angles)
y = np.sin(angles)
plt.plot(x, y, marker='o')
plt.gca().set_aspect('equal')
plt.grid(True)
plt.show()