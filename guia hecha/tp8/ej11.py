""" 
Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales
contiene, identificando la cantidad de cada una. Devolver un diccionario con los
resultados. Luego desarrollar un programa para leer una frase e invocar a la
función por cada palabra que contenga la misma. Imprimir las palabras y la
cantidad de vocales hallada.
"""

"""diccionario = {tuplaA} esta linea redefine el diccionario como un conjunto"""

def contarVocales(palabra): 
    diccionario = {}
    palabra = palabra.upper()

    if "A" in palabra: 
        cantidad = palabra.count("A")
        diccionario["A"] = cantidad
    
    if "E" in palabra: 
        cantidad = palabra.count("E")
        #tuplaE = ("E", cantidad)
        diccionario["E"] = cantidad
 
    if "I" in palabra: 
        cantidad = palabra.count("I")
        diccionario["I"] = cantidad

    if "O" in palabra: 
        cantidad = palabra.count("O")
        diccionario["O"] = cantidad

    if "U" in palabra: 
        cantidad = palabra.count("U")
        diccionario["U"] = cantidad

    return diccionario

hola = contarVocales("esdrujula")
print(hola)