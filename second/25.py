'''Q25. Write a Python program to plot a line graph with markers at all points.'''
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [5,3,6,2,7]
plt.plot(x, y, marker='o')
plt.show()