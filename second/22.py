'''Q22. Write a Python program to draw concentric circles (3 circles).'''
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
for r in [2,4,6]:
    circle = plt.Circle((0,0), r, fill=False)
    ax.add_patch(circle)
    ax.set_aspect('equal')

plt.xlim(-7, 7)
plt.ylim(-7, 7)
plt.show()