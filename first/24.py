'''Q24. Write a Python program to find all extreme points from a list of 2-dimensional points: 
 Leftmost point – point with the smallest x-coordinate 
 Rightmost point – point with the largest x-coordinate 
 Topmost point – point with the largest y-coordinate 
 Bottommost point – point with the smallest y-coordinate 
Use the min() and max() functions with lambda expressions as keys. '''


pts=[(4,2),(1,5),(7,1),(3,9)] 
left=min(pts,key=lambda p:p[0]) 
right=max(pts,key=lambda p:p[0]) 
top=max(pts,key=lambda p:p[1]) 
bottom=min(pts,key=lambda p:p[1]) 

print("leftmost point ",left)
print("rightmost point ",right)
print("topmost point ",top)
print("bottommost point ",bottom)