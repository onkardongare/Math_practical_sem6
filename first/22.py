'''Q22. Write a Python program to find the topmost point from a list of 2-dimensional 
points.A topmost point is the one with the largest y-coordinate. 
Use the max() function with a lambda expression that selects the y-value of each point. '''


pts=[(2,3),(3,9),(4,1)] 
print(max(pts,key=lambda p:p[1])) 