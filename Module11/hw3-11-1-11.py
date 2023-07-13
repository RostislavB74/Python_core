class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index==0:
            Point.x = value
            return Point.x
        if index==1:
            Point.y = value
            return Point.y
         
            

    def __getitem__(self, index):
        if 0 < index< 1:
            if index==0:
                return self.coordinates.x
            if index==1:
                return self.coordinates.y
        return
vector = Vector(Point(1 10))

#print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10

vector[0] = 10  # Встановлюємо координату x вектора 10
print(vector.coordinates.x)
#print(vector[0])
#   # 10
# print(vector[1])  # 10        
vector[2] == 200
print(vector.coordinates.z)
# print(vector.coordinates.x)
# print(vector.coordinates.y)
