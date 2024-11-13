# El método index permite buscar un elemento dentro de una lista, devolviendo la
# posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
# produce una excepción de tipo ValueError. Desarrollar un programa que cargue
# una lista con números enteros ingresados a través del teclado (terminando con -1)
# y permita que el usuario ingrese el valor de algunos elementos para visualizar la
# posición que ocupan, utilizando el método index. Si el número no pertenece a la
# lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
# proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.

def lista(): 
    lista = []
    contadorErrores = 0

    num = int(input("Ingrese el numero que desea agregar a la lista, -1 para finalizar "))
    while num != -1: 
        lista.append(num)
        num = int(input("Ingrese el numero que desea agregar a la lista, -1 para finalizar "))
 
    while True: 
        try: 
            numBuscar = int(input("Ingrese el numero que desea buscar en la lista, -1 para finalizar "))
            while numBuscar != -1: 
                show = lista.index(numBuscar)
                print("La posicion del elemento es ", show)
                numBuscar = int(input("Ingrese el numero que desea buscar en la lista, -1 para finalizar "))    

            else: 
                break

        except ValueError: 
            contadorErrores += 1
            print("el numero que ingresaste no esta en la lista, te quedan ", (3 - contadorErrores), "intentos")
            if contadorErrores == 3: 
                print("llegaste al limite maximo de intentos, abortando ...")
                break
lista()