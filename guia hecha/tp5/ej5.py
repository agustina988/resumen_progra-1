#La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
#módulo math. Escribir un programa que utilice esta función para calcular la raíz
#cuadrada de un número cualquiera ingresado a través del teclado. El programa
#debe utilizar manejo de excepciones para evitar errores si se ingresa un número
#negativo.

import math

def calcularRaiz(): 
    while True: 
        try: 
            numero = float(input("Ingrese su numero "))
            assert numero > 0
            raiz = math.sqrt(numero)
            break

        except AssertionError:
            print("Por favor ingrese un numero positivo ")

        except ValueError: 
            print("Por favor ingrese un numero ")

    print("la raiz de su numero es ", raiz)


calcularRaiz()