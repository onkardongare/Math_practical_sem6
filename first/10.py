'''Q10. Write a method to remove all points from the list in python. 
Program: '''

class PointList:
    def __init__(self):
        self.points=[]

    def remove(self,p):
        if p in self.points:
            self.points.remove(p)

p1=PointList()
p1.points=[(1,2),(3,4),(5,6)]
p1.remove((3,4))

print(p1.points)