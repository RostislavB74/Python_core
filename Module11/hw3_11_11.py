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
        self.index = index
        print(self.index)
        
        if self.index==0:
            x= value
            print(f"x={x}")
            return x
        if self.index==1:
            y= value
            print(f"y={y}")
            return y    #print(f"if {self.coordinates[self.index]}")
        # else:
        #     self.data[key] = [value]
            
        
            

    def __getitem__(self, index):
        pass        
            
vector = Vector(Point(1, 10))
# print(vector.coordinates.x)  # 1
# print(vector.coordinates.y)  # 10
vector[0] = 100
vector[1] = 10  # Встановлюємо координату x вектора 10
#print(vector.coordinates.x)