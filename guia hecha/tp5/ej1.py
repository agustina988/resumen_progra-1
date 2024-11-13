def ingresarNumerosNaturales():   
    while True:
        try: 
            num = int(input("Ingrese un numero "))
            #if isinstance(num, int)

            1/num

            assert num > 0
            break
        except ValueError:
            print("tenias que ingrear un num no un float")

        except ZeroDivisionError: 
            print("0")

        except AssertionError: 
            print("debias ingresar un numero mayor a 0")
    return num
   

ingresarNumerosNaturales()