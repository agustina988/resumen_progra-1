#matriz de prueba simetrica diagonal izquierda
matrizSimetricaPruebaSecundaria = [
    [1, 2, 3, 1],
    [2, 3, 1, 3],
    [3, 1, 3, 2],
    [1, 3, 2, 1]
]

#matriz de prueba
matriz = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]

#matriz de prueba simetrica
matrizSimetricaPrueba = [
    [1,2,3],
    [2,4,5],
    [3,5,6]
]

#matriz de prueba desordenada
matrizDesordenada = [
    [5,2,6,1],
    [9,7,5,3],
    [1,5,3,6],
    [8,1,9,2]
]

#matriz capicua 
matrizCapicua = [
    [1,5,6,4],
    [2,3,4,8],
    [0,0,0,0],
    [2,3,4,5],
    [1,5,6,4]
]

#funcion A
def cargarNumerosEnterosMatriz(): 
    n = int(input("Ingrese la dimension de la matriz (numero entero mayor a 1) "))
    while n < 2: 
        n = int(input("Ingrese la dimension de la matriz (numero entero mayor a 1) "))    
    matriz = [[0] * n for i in range(n)]
    print(matriz)
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas): 
        for c in range(columnas): 
            n = int(input("Ingrese el entero que desea agregar a la lista"))
            while n < 1: 
                n = int(input("Ingrese el entero que desea agregar a la lista"))
            matriz[f][c] = n
    
    return matriz

#funcion B, ordenando de forma ascendente fila a fila
def ordenarMatrizAscendente(matriz): 
    filas = len(matriz)
    for f in range(filas): 
        matriz[f].sort()
    
    mostrarMatriz(matriz)

#funcion C
def intercambiarDosFilas(matriz,filaA, filaB):
     aux = matriz[filaA]
     matriz[filaA] = matriz[filaB]
     matriz[filaB] = aux
     print(matriz)


#funcion D
def intercambiarDosColumnas(matriz,columna1,columna2): 
    filas = len(matriz)
    for f in range(filas): 
        aux = matriz[f][columna2]
        matriz[f][columna2] = matriz[f][columna1]
        matriz[f][columna1] = aux
    
    mostrarMatriz(matriz)

#funcion mostrar
def mostrarMatriz(matriz): 
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):  
            print(matriz[f][c], end = " ")
        print()

#funcion copiar
def copiarMatrices(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matrizDos = [] 
    for f in range(filas): 
        fila = []
        for c in range(columnas): 
            fila.append(matriz[f][c])
        matrizDos.append(fila)
    return matrizDos

#funion e, debe recibir si o si una matriz nxn para no dar error, #millones o incluso, miles de millones 
def trasponerMatriz(matriz): 
    filas = len(matriz)
    columnas = len(matriz[0])
    matrizCopia = copiarMatrices(matriz)
    for f in range(filas): 
        for c in range(columnas): 
            if matriz[f][c] != matrizCopia[f][c]: 
                continue
            else: 
                aux = matriz[f][c] 
                matriz[f][c] = matriz[c][f]
                matriz[c][f] = aux
    mostrarMatriz(matriz)

#funcion f, calcular el promedio de los elementos de una fila 
def calcularPromFila(matriz,fila): 
    filas = len(matriz)
    columnas = len(matriz[0])
    sumador = 0
    for c in range(columnas): 
        sumador += matriz[fila][c]
    promedio = sumador / filas
    print("El promedio de la fila ",fila,"es ", promedio)

#funcion g, calcular el porcentaje de elementos impares en una columna
def calcularPorcImp(matriz,columna): 
    pares = 0 
    impares = 0
    filas = len(matriz)
    for f in range(filas):
        if matriz[f][columna] % 2 != 0: 
            impares += 1
        else: 
            pares += 1
    porcImpares = impares * (pares + impares) / 100
    print(porcImpares)

#funcion h, matriz simetrica con respecto a su diagonal principal 
def verificarSimetriaPrincipal(matriz): 
    filas = len(matriz)
    columnas = len(matriz[0])
    simetria = True
    for f in range(filas): 
        for c in range(columnas): 
            if matriz[f][c] == matriz[c][f]: 
                continue
            else: 
                simetria = False
    return simetria

#funcion i, matriz simetrica con respecto a su diagonal secundaria 
def verificarSimetriaSecundaria(matriz): 
    n = len(matriz) 
    simetria = True
    for f in range(n):
        for c in range(n): 
            print(n - c -1)
            if matriz[f][c] != matriz[n - f - 1][n - c - 1]: 
                simetria = False
                break
        if not simetria: 
            break
    return simetria

verificar = verificarSimetriaSecundaria(matrizSimetricaPruebaSecundaria)
if verificar: 
    print("simetria ")
else: 
    print("asimetria ")

#funcion j, determinar columnas capicuas 
def algo(matriz):
    filas = len (matriz)
    columnas = len(matriz[0])
    columnasCapicua = []

    for c in range(columnas):

        capicua = True

        for f in range(filas // 2): 

            if f == 0: 
                if matriz[f][c] != matriz[-1][c]: 
                    capicua = False

            if matriz[f][c] != matriz[-f -1][c]: 
                capicua = False

        if capicua == True: 
            for f in range(filas): 
                columnasCapicua.append(matriz[f][c])
        
    return columnasCapicua

check = algo(matrizCapicua)
print(check)

#nunca romper un bucle si no es necesario, seguir el ciclo original 
#nigun volumen de datos se almacena en memoria 
