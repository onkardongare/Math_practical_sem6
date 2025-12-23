'''Q7. Write a python programe to add a method add_point(x, y) to insert a new point 
Program: '''

class PointList:
    def __init__(self):
        self.points=[]

    def show(self):
        for p in self.points:
            print(p)

p=PointList()
p.points=[(2,3),(4,1),(7,8)]
p.show()