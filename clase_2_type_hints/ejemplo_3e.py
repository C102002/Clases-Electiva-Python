from typing import Protocol

class SuperHero(Protocol):
    def fly(self) -> None:
        pass

# Esta función acepta cualquier objeto que tenga un método fly() 
# como esrá definido en el protocolo SuperHero
def call_a_hero(hero: SuperHero) -> None:
    # hace una llamada a la clase superhero
    pass

class IronMan(SuperHero):
    def fly(self) -> None:
        print("Ironman comienza a volar")

class SpiderMan:
    def fly(self) -> None:
        print("Spiderman comienza a volar")

class Man:
    def run(self) -> None:
        print("Corriendo")

Tony = IronMan()
Goyo = Man()
Peter = SpiderMan()

call_a_hero(hero=Tony)
call_a_hero(hero=Goyo)
call_a_hero(hero=Peter)