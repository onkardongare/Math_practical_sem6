'''Q14. Write python programe to Count even integer points 
Program: '''

pts=[(2,4),(3,5),(6,8)] 
c=sum(1 for x,y in pts if x%2==0 and y%2==0) 
print(c)