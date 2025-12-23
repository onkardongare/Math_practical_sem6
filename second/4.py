'''Q4. Write a Python program to draw a ray starting from point A and extending
in one direction.'''
import matplotlib.pyplot as plt
plt.scatter(2,2)
plt.text(2.1,2.1,"A")
plt.plot([2,10],[2,2])
plt.xlim(0,12)
plt.ylim(0,5)
plt.grid(True)
plt.show()