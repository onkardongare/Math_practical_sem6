'''Q11. Write a Python program to draw a circle using Matplotlib.
Program:'''
import matplotlib.pyplot as plt
circle = plt.Circle((0,0), 5, fill=False)
fig, ax = plt.subplots()
ax.add_patch(circle)
ax.set_aspect('equal', adjustable='box')
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.show()