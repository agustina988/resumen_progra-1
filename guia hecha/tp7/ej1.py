# 1. Escribir una función que devuelva la cantidad de dígitos de un número entero, sin
# utilizar cadenas de caracteres.

def contarDigitos(numero, n=0):
    if numero > 0: 
        return  contarDigitos(numero //10, n + 1) 
    else: 
        return n
    
    

hola = contarDigitos(100)
print(hola)