'''Q19. Write a Python program to draw a scatter plot of 10 random points.'''
import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(10)
y = np.random.rand(10)
plt.scatter(x, y)
plt.show()