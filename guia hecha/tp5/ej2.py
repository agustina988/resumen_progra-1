#Realizar una función que reciba como parámetros dos cadenas de caracteres con-
#teniendo números reales, sume ambos valores y devuelva el resultado como un
#número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
#utilizando manejo de excepciones para detectar el error

def sumarCadenas(numeroA, numeroB): 

    try:
        
        #float(numeroA, numeroB) ERROR 
        float(numeroA)
        float(numeroB)
        #hola = float(numeroA)
        #hola2 = float(numeroB)
        resu = numeroA + numeroB
        #resu = hola + hola2
        return resu

        #dos prints diferentes dependiendo de que forma utilices, el de los holas funciona como esperaras, el otro no

    except TypeError: 
        return -1


numeroA = input("ingrese su primer numero perri ")
numeroB = input("ingrese su segundo numero perri ")
elperro = sumarCadenas(numeroA, numeroB)
print(elperro)