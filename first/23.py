'''Q23. Write a Python program to find the bottommost point from a list of 2-dimensional 
points.A bottommost point is the one with the smallest y-coordinate.Use the min() function 
with a lambda expression that selects the y-value of each point '''


pts=[(5,2),(1,7),(3,0)] 
print(min(pts,key=lambda p:p[1])) 