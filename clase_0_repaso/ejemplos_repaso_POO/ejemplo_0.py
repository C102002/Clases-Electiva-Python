class Robot:
 
    def __init__(self, name=None, build_year=2000):
        self.name = name
        self.build_year = build_year
        
    def say_hi(self):
        if self.name:
            print("Hey, soy " + self.name)
        else:
            print("Hey, soy un robot sin nombre")
            
    
    def __repr__(self):
        return "Robot('" + self.name + "', " +  str(self.build_year) +  ")"

    def __str__(self):
        return "Name: " + self.name + ", Build Year: " +  str(self.build_year)

     
if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    y = Robot("Caliban", 1943)
    z = Robot()
    for rob in [x, y, z]:
        rob.say_hi()
        if rob.name == "Caliban":
            rob.build_year = 1993
        print("Fui construido en el año " + str(rob.build_year) + "!")
        if rob.name == None:
            print('este robot no tiene nombre')

    print()
    print("Usando __str__():", x)
    print("Usando __repr__():",x.__repr__())
    assert x == eval(repr(x))
    