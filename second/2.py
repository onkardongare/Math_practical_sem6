'''Q2. Write a Python program to display two points A and B on a graph.
Program:'''
import matplotlib.pyplot as plt
x = [1,4]
y = [2,2]
plt.scatter(x, y)
plt.text(1.1,2.1,"A")
plt.text(4.1,2.1,"B")
plt.grid(True)
plt.show()