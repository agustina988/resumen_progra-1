cadenaPrueba = "Esta tarde iremos a pasear por la playa. Mi perro siempre juega con su pelota roja."

# solucion usando slicing
def extraerSubcadena(cadena): 
    inicio = int(input("Ingrese el inicio de la subcadena "))
    cantCaract = int(input("Ingrese la cantidad de caracteres que desea extraer "))
    fin = inicio + cantCaract
    subCadena = cadena[inicio:fin:]

    return subCadena


check = extraerSubcadena(cadenaPrueba)
print(check)

# solucion sin usar rebanadas (indices)
def extraerSubcadena2(cadena): 
    inicio = int(input("Ingrese el inicio de la subcadena "))
    cantCaract = int(input("Ingrese la cantidad de caracteres que desea extraer "))
    fin = inicio + cantCaract
    subCadena = ''

    for i in range(inicio, fin): 
        subCadena += cadena[i]

    return subCadena

check = extraerSubcadena2(cadenaPrueba)
print(check)
