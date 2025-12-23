'''Q29. Write a Python program to calculate distance between 3D 
points. '''


import math
p1 = (1, 2, 3) 
p2 = (4, 6, 8) 

d = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)

print("3D Distance =", d) 