'''Q1. Write a Python program to plot a single point on a graph using Matplotlib.
Program:'''
import matplotlib.pyplot as plt
plt.scatter(2,3,color='red')
plt.text(2.1,3.1,"A")
plt.xlim(0,5)
plt.ylim(0,5)
plt.grid(True)
plt.show()