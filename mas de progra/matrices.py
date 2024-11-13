#---> CREAR

#crear matrices de forma dinamica 
filas = 3
columnas = 4
matriz = []
for f in range(filas): 
    matriz.append([])
    for c in range(columnas): 
        matriz[f].append(0)

#otra forma utilizando replicacion de elementos
for f in range(filas): 
    matriz.append([0] * columnas)

#tambien se pueden crear utilizando listas por comprension
matriz = [[0] * columnas for i in range(filas)]

#----------------------------------------------------------------------------------------------------
#---> RELLENAR  
#suponiendo que tenemos una matriz ya creada con una funcion crearMatriz()

#matriz = crearMatriz()
#filas = len(matriz) # cantidad de filas, osea, para abajo 
#columnas = len(matriz[0]) # con el len de una de las filas sabemos cuantos elementos hay por columna
#for f in range(filas): 
#    for c in range(columnas): 
#        n = int(input("Ingrese un numero "))
#        matriz[f][c] = n

#------------------------------------------------------------------------------------------------------------------------------------------------------
#---> IMPRIMIR 

def imprimirMatriz(matriz): 
    #autodectamos el tamaño de la matriz 
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range (filas): 
        for c in range(columnas): 
            print("%3d" %matriz[f][c], end="")
        print()

imprimirMatriz(matriz)