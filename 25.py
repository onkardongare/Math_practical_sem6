'''Q25. Write a Python program to generate a set of points not in general position in  
          2D  space.            
a) Include at least three collinear points. 
b) Add some random points that may or may not be collinear. 
c) Store the points as tuples in a list and print the list. '''


import random 

# Function to generate random points ( with possible collinearity)
def generate_points_not_general(n):
    pts=[]

    #Add three collinear points along y = 2x + 1
    for x in range(3):
        pts.append((x,2*x+1))

    #Add random points (may or may not be collinear)
    for _ in range(n-3):
        x = random.randint(0,10)
        y = random.randint(0,10)
        pts.append((x,y))
    
    return pts

# Generate 7 points ( 3 collinear + 4 random)
points = generate_points_not_general(7)
print(points)