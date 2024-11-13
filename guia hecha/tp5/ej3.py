#Desarrollar una función que devuelva una cadena de caracteres con el nombre del
#mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
#obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
#Devolver una cadena vacía si el número de mes es inválido. La detección de meses
#inválidos deberá realizarse a través de excepciones.

def detectarMes(numero): 
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    
    try: 
        if numero > 12 or numero < 1: 
            raise ArithmeticError
        
    except ArithmeticError: 
        cadena = "'cadena vacia'"

    else: 
        cadena = meses[numero -1]

    return cadena

check = detectarMes(1)
print(check)

check2 = detectarMes(16)
print(check2)