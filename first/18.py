'''Q18. Write a Python program to sort a list of 2-dimensional points based on their distance 
from the origin (0,0). Use the math.dist() function inside the sorted() key to compute the 
distance of each point. '''

import math 
pts=[(3,4),(1,1),(0,5)] 
print(sorted(pts,key=lambda p:math.dist((0,0),p)))