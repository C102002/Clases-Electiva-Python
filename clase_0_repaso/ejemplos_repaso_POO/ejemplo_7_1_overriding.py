class A:
    def explore(self):
        print("método explore() de la clase A")
 
class B(A):
    def explore(self):
        super().explore()  # llamando al método explore() de la superclase
        print("método explore() de la clase class B")
 
if __name__ == "__main__":
    b_obj = B()
    b_obj.explore()