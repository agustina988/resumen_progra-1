def normalizar(lista):
    suma_total = sum(lista)  # Sumar todos los elementos de la lista
    if suma_total == 0:
        return [0] * len(lista)  # Evitar división por cero si la suma es 0
    return [x / suma_total for x in lista]  # Normalizar cada elemento

# Programa para verificar el comportamiento de la función
def verificar_normalizacion():
    listas_de_prueba = [
        [1, 1, 2,65,234,5,23,5,11,3,7,9,67,74,5],
        [10, 20, 30],
        [0, 0, 0],
        [1, 2, 3, 4],
        [5]
    ]
    
    for lista in listas_de_prueba:
        resultado = normalizar(lista)
        print(f"Lista original: {lista}")
        print(f"Lista normalizada: {resultado}")
        print(f"Suma de elementos normalizados: {sum(resultado)}\n")

# Ejecutar el programa de verificación
verificar_normalizacion()
