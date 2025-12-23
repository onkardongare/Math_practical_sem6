'''Q19. Write a Python program to sort a list of 2-dimensional points based on the sum of 
their coordinates (x + y). Use the sorted() function with a lambda expression that returns 
the sum of each point’s coordinates. '''

pts=[(1,2),(3,1),(5,0)] 
print(sorted(pts,key=lambda p:p[0]+p[1])) 