"""Crear una función generadora llamada progresion_aritmetica que genere los términos de una progresión aritmética. La función debe aceptar tres argumentos:

inicio: float: El primer término de la progresión.
paso: float: La diferencia común entre términos consecutivos.
limite: float | None = None: Un valor opcional. Si se proporciona, la progresión se detendrá antes de generar un término que sea estrictamente mayor que limite. Si es None, el generador debería ser potencialmente infinito (aunque en la práctica se detendrá por otras razones o manualmente)."""

def progresion_aritmetica(inicio:float,paso:float,limite:float | None=1000):
    if limite==None:
        limite=1000
    n=0
    while(inicio<limite):
        yield inicio
        inicio+=paso
        n+=1
    

# Ejemplo de uso
# Generar los primeros 5 términos empezando en 0 con paso 2
gen_pa = progresion_aritmetica(inicio=0.0, paso=2.0)
primeros_cinco = [next(gen_pa) for _ in range(5)]
print(f"Primeros 5: {primeros_cinco}") # Esperado: [0.0, 2.0, 4.0, 6.0, 8.0]

# Generar términos hasta (sin incluir) 10, empezando en 1 con paso 1.5
gen_limitado = progresion_aritmetica(inicio=1.0, paso=1.5, limite=10.0)
print(f"Hasta 10: {list(gen_limitado)}") # Esperado: [1.0, 2.5, 4.0, 5.5, 7.0, 8.5]