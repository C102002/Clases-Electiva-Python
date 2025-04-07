class MyClass:
    def method(self):
        return 'llamado el método de instancia', self

    @classmethod
    def classMethod(cls):
        return 'llamado el método de clase', cls

    @staticmethod
    def staticMethod():
        return 'llamado el método statico'
    
if __name__ == '__main__':
    obj1 = MyClass()
    
    string, obj = obj1.method()
    print(string, obj)
    print()
    
    print(obj1.classMethod())
    print(MyClass.classMethod())
    print()
    
    print(obj1.staticMethod())    
    print(MyClass.staticMethod())
    
# ver explicación detallada en https://realpython.com/instance-class-and-static-methods-demystified/

    