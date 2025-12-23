'''Q30. Write a Python program to print distance between each pair of points in a list. 
Explain loops.  '''


import math

points = [(1, 2), (4, 6), (7, 3)]

for i in range(len(points)-1):
    p1 = points[i]
    p2 = points[i+1]
    d = math.dist(p1, p2)
    print(f"Distance between {p1} and {p2} is {d}")