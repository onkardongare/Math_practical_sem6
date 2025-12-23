'''Q17. Write a Python program to draw a bar graph of student marks.
Program:'''
import matplotlib.pyplot as plt
students = ['A', 'B', 'C', 'D', 'E']
marks = [78,85,92,66,74]
plt.bar(students,marks)
plt.show()