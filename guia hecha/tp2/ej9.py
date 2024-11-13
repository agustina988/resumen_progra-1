#9. Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
#   que no sean múltiplos de 5. A y B se ingresar desde el teclado

def listaPorComprension(A,B): 
    lista = [i for i in range(A,B) if i % 7 == 0 and i % 5 != 0]
    print(lista)

A = int(input("Ingrese A "))

B = int(input("Ingrese B "))

listaPorComprension(A,B)
