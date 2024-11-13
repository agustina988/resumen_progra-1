#Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
#las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
#un programa para imprimir los números enteros entre 1 y 100 000, y que solicite
#confirmación al usuario antes de detenerse cuando se presione Ctrl-C.

def imprimirNumeros(): 
    while True:
        try: 
            for i in range(100000): 
                print(i)
                ultimaPos = i

        except KeyboardInterrupt: 
            print("realmente desea interrumpir la ejecucion del programa? ")
            eleccion = int(input("ingrese 1 para si 0 para no "))
            if eleccion == 1: 
                break
            else: 
                pass

imprimirNumeros()