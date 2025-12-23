'''Q26. Write a Python program to find the distance between two points in a 2D plane.  
Answer: '''

import math

x1,y1=2,3
x2,y2=8,7

distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

print("Distance = ",distance)