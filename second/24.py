'''Q24. Write a Python program to plot a pie chart of 5 categories.'''
import matplotlib.pyplot as plt
sizes = [20,25,15,30,10]
labels = ['A','B','C','D','E']
plt.pie(sizes, labels=labels)
plt.show()