'''Q15. Write a Python program to draw a parabola (y = x2).'''
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 400)
y = x**2
plt.plot(x, y)
plt.grid(True)
plt.show()