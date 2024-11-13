# contar la cantidad de veces que aparece un valor dentro de una matriz

def contarValor(matriz, valor, i = 0, cantidad = 0): 

    if i == len(matriz): 
        return cantidad
    
    cantidad += matriz[i].count(valor)
    print(cantidad)
        
    contarValor (matriz, valor, i +1, cantidad)

matriz = [[1,5,6],
          [5,9,0],
          [1,2,3]]
    
cantidad = contarValor(matriz,5)
print(cantidad)