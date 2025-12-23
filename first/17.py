'''Q17. Write a Python program to sort a list of 2-dimensional points in descending order of 
their x-coordinate. Use the sorted() function with a lambda function as the key and set 
reverse=True. '''

pts=[(1,4),(3,1),(2,2)] 
print(sorted(pts,key=lambda p:p[0],reverse=True)) 