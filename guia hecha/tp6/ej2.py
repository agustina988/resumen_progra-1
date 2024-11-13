"""ejercicio"""
#Escribir un programa que permita dividir un archivo de texto cualquiera en partes
#que se puedan enviar por correo electrónico. El tamaño máximo de las partes se
#ingresa por teclado. Los nombres de los archivos generados deben respetar el
#nombre original con el agregado de un sufijo que indique de qué parte se trata.
#Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuar-
#se después del delimitador del mismo. Mostrar un mensaje de error si el proceso no
#pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en
#memoria

"""resolucion"""
# parte del codigo clave que me lleva a la resolucion consultar a la profe que onda 
# parece ser la forma de crear diferentes archivos con nombre variable sin conocer la cantidad de archivos que seran creados previamente 
# --->     nombre_archivo = f"parte_{contador}.txt"

def dividirArchivos(): 
    cantLineas = 0
    while True: 
        try: 
            print("Hola! ingresa la cantidad maxima ")
            print("de registros que que contendra cada parte del archivo ")
            registrosMax = int(input("... "))
            break
        except ValueError: 
            print("Por favor ingrese un int al input ")

    try: 
        arch = open("/home/luciowo/progra_1/ejericios_guia/tp6/ej2/archivoLeer.txt", mode = 'rt')

    except IOError: 
        print("El archivo no se pudo abrir correctamente ")

    else: 

        linea = arch.readline()
        while linea: 
            cantLineas += 1
            print("va por aca")
            linea = arch.readline()

        try: 
            arch.close()
        except IOError: 
            print("el archivo no se pudo cerrar correctamente ")
        
        cantArchivos = cantLineas / registrosMax
        if type(cantArchivos) == float: 
            int(cantArchivos)
            cantArchivos += 1
        
        #----------#

        arch = open("/home/luciowo/progra_1/ejericios_guia/tp6/ej2/archivoLeer.txt", mode = 'rt')
        contadorArchivos = 1
        while contadorArchivos <= cantArchivos:
            nombre_archivo = f"parte_{contadorArchivos}.txt"
            contadorRegistros = 1
            try:
                archivoEscribir = open(nombre_archivo, 'wt') 
            except IOError: 
                print(f"el archivo {nombre_archivo} no se pudo abrir correctamente ")
            else:
                    
                while contadorRegistros <= registrosMax:
                    linea = arch.readline()
                    archivoEscribir.write(linea)
                    contadorRegistros += 1
                archivoEscribir.close()
                contadorArchivos += 1

        else: 
            try: 
                arch.close()
                print("fin de el programa")
            except IOError: 
                print("El archivo no se pudo cerrar correctamente")


dividirArchivos()