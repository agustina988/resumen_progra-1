def remplazarPalabras(cadena, palabra, reemplazo): 
    ocurrencias = cadena.count(palabra)
    cadena = cadena.replace(palabra, reemplazo)
    return cadena, ocurrencias

cadena = "Ojala gargajo bajo conseguir trabajo el año que viene me gustaria mucho tener trabajo trabajo trabajo la cadena tiene que tener varias veces la palabra trabajo asi que voy a seguir escribiendo trabajo"

palabra = 'trabajo'

reemplazo = 'gato'

check = remplazarPalabras(cadena, palabra, reemplazo)[0]

print(check)

check = remplazarPalabras(cadena, palabra, reemplazo)[1]

print(check)

#super intereante esto, con los corchetes se puede especificar que valor del return mostrar