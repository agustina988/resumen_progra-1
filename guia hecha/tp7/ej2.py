# Desarrollar una función que reciba un número binario y lo devuelva convertido a
# base decimal.

# Toma cada dígito del número binario.
# Multiplica cada dígito por 2 elevado a la potencia de su posición (contando desde la derecha, empezando en 0).
# Suma todos los resultados.


def binarioDecimal(decimal = 0, binario = 0, i = 0): 
    binario = str(binario)
    if len(binario) == 0: 
        return decimal 
    print("valor de i ", i, "valor de decimal, ",decimal, "valor de binario ", binario)
    return binarioDecimal(decimal + (int(binario[-1]) * (2 ** i)), binario[:-1], i +1)

## no se pueden usar += dentro de las llamadas recursivas 

a =binarioDecimal(0, 1001, 0)
print(a)