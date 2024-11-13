"""
Escribir una función buscarclave() que reciba como parámetros un diccionario y un
valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el dic-
cionario. Comprobar el comportamiento de la función mediante un programa apro-
piado
"""

def buscarClave(diccionario, valor): 
    listaClaves = []
    for clave in diccionario: 
        if diccionario[clave] == valor: 
            listaClaves.append(clave)


    return listaClaves 


diccionario = {1:555,2:555,3:555,4:555,321:52,77:12}
valor = 555

lista = buscarClave(diccionario, valor)
print(lista)