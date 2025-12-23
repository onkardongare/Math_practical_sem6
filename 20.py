'''Q20. Write a Python program to find the leftmost point from a list of 2-dimensional 
points.A leftmost point is the point having the smallest x-coordinate.Use the min() 
function with a lambda expression as the key. '''

pts=[(4,2),(1,5),(3,6)] 
print(min(pts,key=lambda p:p[0])) 