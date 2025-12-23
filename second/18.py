'''Q18. Write a Python program to draw a line graph showing monthly
temperatures. give me word file with program anser with output'''
import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
temp = [20,22,28,32,35,30]
plt.plot(months, temp)
plt.show()