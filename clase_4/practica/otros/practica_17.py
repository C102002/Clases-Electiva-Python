"""
Se tiene una lista con diversos valores de tipo string. Se desea crear un programa que le pregunte al usuario sobre una entrada de tipo string. Si el dato ingresado se encuentra en el arreglo, debe indicar el índice de posicionamiento. De no encontrarlo debe indicar “No encontrado”. Use los siguientes datos:

datos = “niño”, "pelota", "corneta", "guitarra", "flor", "casa", "caballo"

"""

datos = ["niño", "pelota", "corneta", "guitarra", "flor", "casa", "caballo"]

def find_entry(entry_data:str)->str:
    if entry_data not in datos:
        return f"No encontrado"
    data=datos.index(entry_data)
    return data


result_1=find_entry("pelota")
print(f"resukt_1:{result_1}")


result_2=find_entry("antonio")
print(f"resukt_2:{result_2}")