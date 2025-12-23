'''Q21. Write a Python program to find the rightmost point from a list of 2-dimensional 
points.A rightmost point is the point having the largest x-coordinate.Use the max() 
function with a lambda expression as the key. '''


pts=[(1,2),(8,3),(4,1)] 
print(max(pts,key=lambda p:p[0])) 