'''Q9. Write a method to count how many unique points exist in python. 
Program: '''

class PointList:
    def __init__(self):
        self.points=[]

    def add_unique(self,x,y):
        if (x,y) not in self.points:
            self.points.append((x,y))

p1=PointList()
p1.add_unique(1,2)
p1.add_unique(1,2)
p1.add_unique(3,4)

print(p1.points)