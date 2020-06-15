import math
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, target):
        x_diff = target.x - self.x
        y_diff = target.y - self.y
        
        result = math.sqrt(x_diff + y_diff)

        return "The distance is {0:.2f}".format(result)
    
while True:
    try:
        x1 = float(input('>>> x1 = '))
        break
    except:
        print('must be an integer or a float ...')

while True:
    try:
        y1 = float(input('>>> y1 = '))
        break
    except:
        print('must be an integer or a float ...')

while True:
    try:
        x2 = float(input('>>> x2 = '))
        break
    except:
        print('must be an integer or a float ...')
        
while True:
    try:
        y2 = float(input('>>> y2 = '))
        break
    except:
        print('must be an integer or a float ...')

point1 = Point(x1, y1)
point2 = Point(x2, y2)

print(point1.distance(point2))