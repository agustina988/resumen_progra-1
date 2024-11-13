cadenaPrueba = "El tren llegó a la estación a tiempo hoy."

# solucion usando slicing
def eliminarSubcadena(cadena): 
    inicio = int(input("Ingrese el inicio de la subcadena que desea eliminar "))
    cantCaract = int(input("Ingrese la cantidad de caracteres que desea eliminar "))

    fin = inicio + cantCaract
    subCadena = cadena[inicio:fin:]

    cadena = cadena.replace(subCadena, ' ')

    return cadena

check = eliminarSubcadena(cadenaPrueba)
print(check)

# solucion sin usar rebanadas (indices)
def eliminarSubcadena2(cadena): 
    inicio = int(input("Ingrese el inicio de la subcadena que desea eliminar "))
    cantCaract = int(input("Ingrese la cantidad de caracteres que desea eliminar "))
    fin = inicio + cantCaract
    listaLetras = [letra for letra in cadena]
    subCadena = ''
    for i in range(0, inicio): 
        subCadena += listaLetras[i]
    for i in range(fin,len(cadena)): 
        subCadena += listaLetras[i]
    
    return subCadena

check = eliminarSubcadena2(cadenaPrueba)
print(check)

