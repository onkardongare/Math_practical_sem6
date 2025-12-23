'''Q6. Write a Python program to Create PointList and add points. 
Program: '''

class PointList:
    def __init__(self):
        self.points=[]
    def add(self,x,y):
        self.points.append((x,y))

p=PointList()
p.add(1,2)
p.add(3,4)
p.add(5,6)

print(p.points)