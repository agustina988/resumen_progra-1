#todos los numeros impares entre 100 y 200
def listaPorComprension(): 
    lista = [i ** 1 for i in range(100,200) if i % 2 != 0]
    print(lista)
    
listaPorComprension() 
        