class Animal:

    name__clase="nombre clase"
    
    
    def __init__(self, name=None, species=[]):
        self.__name = name
        self.__species = species
    
    def get_name(self):
        return self.__name
    
    def get__species(self):
        return self.__species
    
    # Factory method
    @staticmethod
    def create_vacio():
        return Animal()
    
    # Factory method
    # @classmethod
    # Los dos funcionan igual
    # def create_lleno(self, name=None, species=[]):
        # return Animal(name, species)
        
    # Factory method
    @classmethod
    def create_lleno(cls, name=None, species=[]):
        return Animal(name, species)

if __name__ == "__main__":
    a= Animal("perro",["mamifero","carnivoro"])
    print(f"el animal es {a.get_name()} y su especie es {a.get__species()}")
    b= Animal.create_vacio()
    c= Animal.create_lleno("gato",["mamifero","carnivoro"])
    print(f"el animal es {b.get_name()} y su especie es {b.get__species()}")
    print(f"el animal es {c.get_name()} y su especie es {c.get__species()}")