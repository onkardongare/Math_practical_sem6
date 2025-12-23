'''Q16. Write a Python program to store a list of 2D points and then sort them in ascending 
order of their y-coordinate. '''

pts=[(1,7),(2,3),(4,9)] 
print(sorted(pts,key=lambda p:p[1])) 