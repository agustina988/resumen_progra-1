"""
Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario
y una lista de claves. La función debe eliminar del diccionario todas las claves
contenidas en la lista, devolviendo el diccionario modificado y un número entero
que represente la cantidad de claves eliminadas. Desarrollar también un programa
para verificar su comportamiento
"""

def eliminarClaves(diccionario, listaClaves):
    eliminados = 0
    for i in range(len(listaClaves)): 
        if listaClaves[i] in diccionario:
            del diccionario[listaClaves[i]] 
            eliminados += 1
        else: 
            continue

    return diccionario, eliminados



persona = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid', 'profesión': 'Ingeniero', 'estado_civil': 'Soltero'}
claves_seleccionadas = ['nombre', 'edad', 'ciudad']

diccionario, eliminados = eliminarClaves(persona, claves_seleccionadas)

print(diccionario, eliminados)