def encontrarOcurrencias(cadena, palabra): 
    cadena = cadena.lower()
    palabra = palabra.lower()
    listaPalabra = [letra for letra in palabra]
    contador = 0
    ocurrencias = 0
    for i in range(len(cadena)): 
        if cadena[i] == listaPalabra[contador]: 
            contador += 1
            if contador == len(listaPalabra): 
                ocurrencias += 1
                contador = 0
    
    return ocurrencias

cadena = 'Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.'
palabra = 'UADE'

check = encontrarOcurrencias(cadena,palabra)
print(check)
