# usando la solución mro
# ver explicación aqui: https://medium.com/@__hungrywolf/mro-in-python-3-e2bcd2bd6851s

class A:
    def m(self):
        print("llamado m de A")

class B(A):
    def m(self):
        print("llamado m de B")
        super().m()
        
    
class C(A):
    def m(self):
        print("llamado m de C")
        super().m()
        

class D(B,C):
    def m(self):
        print("llamado m de D")
        super().m()

if __name__ == "__main__":
    x = D()
    x.m()        