# Escribir un programa que juegue con el usuario a adivinar un número. El programa
# debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para
# eso, cada vez que se introduce un valor se muestra un mensaje indicando si el nú-
# mero que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
# adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar
# el número. Si el usuario introduce algo que no sea un número se mostrará un
# mensaje en pantalla y se lo contará como un intento más
import random

def adivinarNumero(): 
    cantidadIntentos = 0
    numero = random.randint(1, 500)
    print("Bienvenido usuario, debe eliminar el numero secreto, este se encuentra entre 1 y 500. Adelante! ")

    while True: 
        try:    
            intento = int(input("Ingrese el numero que cree que es "))
            while intento != numero:
                if intento < numero:   
                    print("El numero introducido es menor al numero que debes encontrar ")
                else: 
                    print("El numero introducido es mayor al numero que debes encontrar ")

                cantidadIntentos += 1
                if cantidadIntentos > 10: 
                    print("mas de 10 intentos ya flaco dale metele ganas ")
                
                intento = int(input("Ingrese el numero que cree que es "))

            else: 
                print("felicitaciones, encontraste el numero en tan solo ", cantidadIntentos, "Intentos ")
                break
        except ValueError: 
            print("Debias ingresar un numero, no una letra! esto cuenta como un intento mas ") 
            cantidadIntentos += 1         

adivinarNumero()