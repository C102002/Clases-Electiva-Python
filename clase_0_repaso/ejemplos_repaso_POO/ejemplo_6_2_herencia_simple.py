class Robot:
    
    def __init__(self, name):
        self.name = name
        
    def say_hi(self):
        print("Hi, I am " + self.name)
        
class PhysicianRobot(Robot):
    pass

class OtroRobot(PhysicianRobot):
    pass

if __name__ == "__main__":
    x = Robot("Marvin")
    y = PhysicianRobot("James")
    print(x, type(x))
    print(y, type(y))
    y.say_hi()

    print("***** type y isinstance *****")
    print(isinstance(x, Robot), isinstance(y, Robot))
    print(isinstance(x, PhysicianRobot))
    print(isinstance(y, PhysicianRobot))
    print(type(y) == Robot, type(y) == PhysicianRobot)