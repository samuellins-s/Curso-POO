class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = int(radius) 

point = Point(150, 100)
circulo1 = Circle(point, 75)

def point_in_circle(circle, point):
    if point in :