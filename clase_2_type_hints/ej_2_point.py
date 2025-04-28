import math
 
class Point:
 
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y   
 
    # get de la coordenada x
    @property
    def x(self):
        return self.__x
 
    # set de la coordenada x
    @x.setter
    def x(self, x):
        self.__x = x
 
    # get de la coordenada y
    @property
    def y(self):
        return self.__y
 
    # set de la coordenada y
    @y.setter
    def y(self, y):
        self.__y = y
 
    # get de la position actual
    @property
    def position(self):
        return self.__x, self.__y
 
    # cambia x e y por a y b
    def move(self, a, b):
        self.__x += a
        self.__y += b
 
    # sobreescribiendo + operator
    def __add__(self, point_obj):
        return Point(self.__x + point_obj.__x, self.__y + point_obj.__y)
 
    # sobreescribiendo - operator
    def __sub__(self, point_obj):
        return Point(self.__x - point_obj.__x, self.__y - point_obj.__y)
 
    # sobreescribiendo < operator
    def __lt__(self, point_obj):
        return math.sqrt(self.__x ** 2 + self.__y ** 2) < math.sqrt(point_obj.__x ** 2 + point_obj.__y ** 2)
 
    # sobreescribiendo <= operator
    def __le__(self, point_obj):
        return math.sqrt(self.__x ** 2 + self.__y ** 2) <= math.sqrt(point_obj.__x ** 2 + point_obj.__y ** 2)
 
    # sobreescribiendo > operator
    def __gt__(self, point_obj):
        return math.sqrt(self.__x ** 2 + self.__y ** 2) > math.sqrt(point_obj.__x ** 2 + point_obj.__y ** 2)
 
    # sobreescribiendo >= operator
    def __ge__(self, point_obj):
        return math.sqrt(self.__x ** 2 + self.__y ** 2) >= math.sqrt(point_obj.__x ** 2 + point_obj.__y ** 2)
 
    # sobreescribiendo == operator
    def __eq__(self, point_obj):
        return math.sqrt(self.__x ** 2 + self.__y ** 2) == math.sqrt(point_obj.__x ** 2 + point_obj.__y ** 2)
 
    ## sobreescribiendo __str__ function
    def __str__(self):
        return "El objeto Point está en: (" + str(self.__x) + ", " + str(self.__y) + ")"
    
    ## sobreescribiendo __repr__ function
    def __repr__(self):
        return "Point(" + str(self.__x) + ", " + str(self.__y) + ")"
 

if __name__ == "__main__":

    p1 = Point(4, 6)
    p2 = Point(10, 6)

    print(f"p1 está en la posición {p1.position}")
    print(f"p2 está en la posición {p2.position}")
    
    print("es p1 < p2 ?", p1 < p2)   # p1 < p2 Es equivalent to p1.__lt__(p2)
    print("Es p1 <= p2 ?", p1 <= p2)  # p1 <= p2 Es equivalent to p1.__le__(p2)
    print("Es p1 > p2 ?", p1 > p2)   # p1 > p2 Es equivalent to p1.__gt__(p2)
    print("Es p1 >= p2 ?", p1 >= p2)   # p1 >= p2 Es equivalent to p1.__ge__(p2)
    print("Es p1 == p2 ?", p1 == p2)   # p1 < p2 Es equivalent to p1.__eq__(p2)
    
    p3 = p1 + p2  # p1 + p2 es equivalent to p1.__add__(p2)
    p4 = p1 - p2  # p1 - p2 es equivalent to p1.__sub__(p2)
    
    print()  # print una línea vacía
    print(p1)  # print(p1) es equivalent to print(p1.__str__())
    print(p2)  # print(p2) es equivalent to print(p2.__str__())
    print(p3)  # print(p3) es equivalent to print(p3.__str__())
    print(p4)  # print(p4) es equivalent to print(p4.__str__())
    print(p4.__repr__())
