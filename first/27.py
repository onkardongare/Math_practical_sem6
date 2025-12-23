'''Q27. Write a Python program to calculate distance between two points using a 
function. '''

import math 

def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1) ** 2)

print("Distance = ",distance(1,2,6,5))

