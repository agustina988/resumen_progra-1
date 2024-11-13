import re 

cadena = "El gato negro duerme en el sillón cómodo 5"

#solucion 1, solo bucles
def filtrarPalabras(cadena):

    primer_numero = re.search(r'\d+', cadena)
    if primer_numero:
        n = (int(primer_numero.group())) 
    print(n)

    listaPalabras = cadena.split()
    cadenaNueva = ''

    for i in range(len(listaPalabras)): 
        if len(listaPalabras[i]) >= n: 
            cadenaNueva += listaPalabras[i]
            cadenaNueva +=  ' '

    print(cadenaNueva)

#solucion 2, listas por comprension
def filtrarPalabras2(cadena):

    primer_numero = re.search(r'\d+', cadena)
    if primer_numero:
        n = (int(primer_numero.group())) 
    print(n)

    listaPalabras = cadena.split()
    cadenaNueva = ''

    cadenaNueva = [palabra for palabra in listaPalabras  if len(palabra) >= n]

    stringNuevo = ''

    for i in range(len(cadenaNueva)):  
        stringNuevo += cadenaNueva[i]
        stringNuevo +=  ' '

    print(stringNuevo)

#solucion 3, funcion filter
def esMayor(string): 
    cadena = "Mañana iremos al parque a jugar fútbol. 5"
    primer_numero = re.search(r'\d+', cadena)
    if primer_numero:
        n = (int(primer_numero.group())) 
    return len(string) > n 

listaPalabras = cadena.split()
check = list(filter(esMayor, listaPalabras))
print(check)

