'''Q12. Write a Python program to draw a rectangle.
Program:'''
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
rect = plt.Rectangle((1,1),4,2,fill=False)
ax.add_patch(rect)
plt.xlim(0,7)
plt.ylim(0,5)
plt.show()