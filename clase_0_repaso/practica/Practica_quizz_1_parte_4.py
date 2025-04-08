# Defina un diccionario llamado informacion_persona, que contengainformación básica de una persona: nombre, edad, ciudad y correoelectrónico.
# En el mismo código cree una variable que acceda a la información de edad y la imprima en el terminal de la computadora

class Persona:
    def __init__(self,nombre,edad,ciudad,correoelectronico):
        self.__nombre=nombre
        self.__edad=edad
        self.__ciudad=ciudad
        self.__correoelectronico=correoelectronico
    # Cambiar el método a público para acceder a la edad
    def getEdad(self):
        return self.__edad
# OJO ESTARIA MAL PORQUE EL SOLO QUIERE EL DICCIONARIO

if __name__ == "__main__":
    informacion_persona={1:Persona("pepe",12,"caracas","pepe@ppee.com")}
    for i,j in informacion_persona.items():
        print(f"la edad del usuario es {j.getEdad()}")
    
    # Correcto
    informacion_persona_correcta={"nombre":"Alfredo", "edad":22, "ciudad":"Caracas", "correoelectronico":"alfredo@gmail.com"}
    print(informacion_persona_correcta["edad"]) 
