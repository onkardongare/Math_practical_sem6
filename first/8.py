'''Q8. Write a method count_points() that returns total points Program in python. '''

class PointList:
    def __init__(self):
        self.points=[]

p=PointList()
p.points=[(1,1),(2,2),(3,3),(4,4)]

print("Total = ",len(p.points))