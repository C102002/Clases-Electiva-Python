class P:

    def __init__(self,x):
        self.__x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

if __name__ == "__main__":
    p1 = P(1001)
    p2 = P(0)
    p2.x = 1500
    print(p1.x, p2.x)
    p1.x = -12
    print(p1.x)