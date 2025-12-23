'''Q14. Write a Python program to draw an X–Y axis manually using plotting.'''
import matplotlib.pyplot as plt
plt.axhline(0)
plt.axvline(0)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()
