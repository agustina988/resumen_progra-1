def crearListaCuadrados(): 
    cantidadElementos = int(input("ingresa N "))
    cuadrados = []
    for i in range(1,cantidadElementos +1): 
        cuadrados.append(i**2)
    print(cuadrados)
    for i in range(1,11): 
        print(cuadrados[-i])

crearListaCuadrados()