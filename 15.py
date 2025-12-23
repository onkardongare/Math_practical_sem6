'''Q15. Write a Python program to store a list of 2D points and then sort them in ascending 
order of their x-coordinate. '''

pts=[(4,1),(1,3),(2,2)] 
print(sorted(pts,key=lambda p:p[0])) 