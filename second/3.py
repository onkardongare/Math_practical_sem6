'''Q3. Write a Python program to draw a line segment between points A and B.
Program:'''
import matplotlib.pyplot as plt
x = [1,5]
y = [3,3]
plt.plot(x, y, marker='o')
plt.text(1,3.1,"A")
plt.text(5,3.1,"B")
plt.grid(True)
plt.show()