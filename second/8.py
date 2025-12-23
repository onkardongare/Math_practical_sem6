'''Q8. Write a Python program to draw a square.
Program:'''
import matplotlib.pyplot as plt
x = [1,5,5,1,1]
y = [1,1,5,5,1]
plt.plot(x, y, marker='o')
plt.grid(True)
plt.show()