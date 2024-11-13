# 3. Escribir una función que devuelva la suma de los N primeros números naturales.

def sumarNaturales (suma = 0, n = 10): 
    if n == 0: 
        return suma
    return sumarNaturales(suma + n, n -1)

apa = sumarNaturales()
print(apa)