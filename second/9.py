'''Q9. Write a Python program to draw perpendicular lines (horizontal &
vertical).'''
import matplotlib.pyplot as plt
plt.plot([-5, 5], [0, 0])
plt.plot([0, 0], [-5, 5])
plt.grid(True)
plt.show()