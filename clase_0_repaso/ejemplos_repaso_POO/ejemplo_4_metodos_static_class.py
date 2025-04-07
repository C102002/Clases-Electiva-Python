class Fraction(object):

    def __init__(self, n, d):
        self.numerator, self.denominator = Fraction.reduce(n, d)

    def prueba(self, a,b):
        return self.mcd(a, b)
        
    @staticmethod
    def mcd(a,b):
        while b != 0:
            a, b = b, a%b
        return a

    @classmethod
    def reduce(cls, n1, n2):
        m = cls.mcd(n1, n2)
        return (n1 // m, n2 // m)

    def __str__(self):
        return str(self.numerator)+'/'+str(self.denominator)

if __name__ == "__main__":
    x = Fraction(8,24)
    print(x)

    y = Fraction(16, 48)
    print(y.prueba(1,2))
    