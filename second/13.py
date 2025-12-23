'''Q13. Write a Python program to plot 5 random points on a graph.'''
import matplotlib.pyplot as plt
import random
x = [random.randint(1, 10) for _ in range(5)]
y = [random.randint(1, 10) for _ in range(5)]
plt.scatter(x, y)
plt.show()