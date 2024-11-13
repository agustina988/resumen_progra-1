# desarrollar una funcion para contar cuantas vocales posee una cadena 

def contarVocales(cadena = "cadena", cantidadVocales = 0, i = 0): 
    cadena = cadena.upper()
    
    if i == len(cadena): 
        return cantidadVocales

    if cadena[i] == "A" or cadena[i] == "E" or  cadena[i] == "I" or cadena[i] == "O" or cadena[i] == "U": 
        cantidadVocales += 1

    return contarVocales(cadena, cantidadVocales, i+1)


holayomellamojuan = contarVocales("zapatilla")
print(holayomellamojuan)