class Robot:
    
    def __init__(self, name):
        self.name = name
        
    def say_hi(self):
        print("Hola, soy " + self.name)
        
class PhysicianRobot(Robot):
    def say_hi(self):
        print("Todo estará muy bien! ") 
        print(self.name + " cuida de ti!")

if __name__ == "__main__":
    y = PhysicianRobot("James")
    y.say_hi()

    print("llamando al método de la superclase")
    print("... y como es 'tradicional' en los robot saludamos :-)")
    Robot.say_hi(y)