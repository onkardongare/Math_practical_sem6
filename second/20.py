'''Q20. Write a Python program to draw a histogram of 100 random numbers.'''
import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(100)
plt.hist(data, bins=10)
plt.show()