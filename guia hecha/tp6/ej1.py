# Escribir un programa que lea un archivo de texto conteniendo un conjunto de ape-
# llidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
# ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cade-
# na "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los
# terminados en "EZ". Descartar el resto. Ejemplo:
# Arslanian, Gustavo –> ARMENIA.TXT
# Rossini, Giuseppe –> ITALIA.TXT
# Pérez, Juan –> ESPAÑA.TXT
# Smith, John –> descartar
# El archivo puede ser creado mediante el Block de Notas o el cualquier otro editor

def guardarApellidos(): 
    archivoEspaña = "españa.txt"
    archivoItalia = "italia.txt"
    archivoArmenia = "armenia.txt"
    try: 
        arch = open("/home/luciowo/progra_1/ejericios_guia/tp6/ej1/nombresApellidos.txt", mode = 'rt')

    except IOError: 
        print("El archivo nombres y apellidos no se pudo abrir correctamente ")

    else: 

        linea = arch.readline()
        
        while linea: 
            print("esta aca")
            lin = linea.strip().split(",")
            apellido = lin[0]
            apellido = apellido.upper()
            armenio = True
            while armenio: 
                if apellido[-1] != "N": 
                    armenio = False
                if apellido[-2] != "A": 
                    armenio = False
                if apellido[-3] != "O": 
                    armenio = False

            if armenio: 
                
                try: 
                    archivoArmeniaAbierto = open(archivoArmenia, mode = 'wt')
                except IOError: 
                    print("No se pudo abrir el archivoArmenia con exito ")
                
                else: 
                    archivoArmeniaAbierto.write(linea + "\n")
                    try: 
                        archivoArmeniaAbierto.close()
                    except IOError: 
                        print("El arhcivoArmenia no se pudo cerrar ")
            
                linea = arch.readline()
                continue
        #########################################################################################

            italiano = True
            while italiano: 
                if apellido[-1] != "I": 
                    italiano = False
                if apellido[-2] != "A": 
                    italiano = False
                if apellido[-3] != "N": 
                    italiano = False

            if italiano: 
                try: 
                    archivoItaliaAbierto = open(archivoItalia, mode = 'wt')
                except IOError: 
                    print("No se pudo abrir el archivoItalia con exito ")
                
                else: 
                    archivoItaliaAbierto.write(linea + "\n")
                    try: 
                        archivoItaliaAbierto.close()
                    except IOError: 
                        print("El archivoItalia no se pudo cerrar correctamente")

                linea = arch.readline()
                continue

        #######################################################################################

            español = True
            while español: 
                if apellido[-1] != "N": 
                    español = False
                if apellido[-2] != "A": 
                    español = False
                if apellido[-3] != "O": 
                    español = False

            if español: 
                try: 
                    archivoEspañaAbierto = open(archivoEspaña, mode = 'wt')
                except IOError: 
                    print("No se pudo abrirEspaña el archivo con exito ")
                
                else: 
                    archivoEspañaAbierto.write(linea + "\n")
                    try: 
                        archivoEspañaAbierto.close()

                    except IOError: 
                        print("El archivoEspaña no se pudo cerrar correctamente")

                linea = arch.readline()
                continue    
        
            linea = arch.readline()

        else: 
            try: 
                arch.close()
            except IOError: 
                print("El archivo nombres y apellidos no se pudo cerrar correctamente ")

    return archivoArmenia, archivoItalia, archivoEspaña


def mostrarApellidos(archivoArmenia, archivoItalia, archivoEspaña): 
    print("llego")
    try: 
        archivoArmeniaAbierto = open(archivoArmenia, mode = 'rt')
    except IOError: 
        print("No se pudo abrir el archivoArmenia con exito nooo aca")

    else: 
        #linea = archivoArmenia.readline()
        #while linea: 
        #    print(linea)
        #    linea = archivoArmenia.readline()
        for linea in archivoArmeniaAbierto: 
            print(linea)
            print(linea.strip())

        try: 
            archivoArmeniaAbierto.close()

        except IOError: 
            print("No se pudo cerrar correctamente el archivoArmenia ")

###############################################################################################    

    try: 
        archivoItaliaAbierto = open(archivoItalia, mode = 'rt')
    except IOError: 
        print("No se pudo abrir el archivoItalia con exito ")

    else: 
        linea = archivoItaliaAbierto.readline()
        while linea: 
            print(linea)
            linea = archivoItaliaAbierto.readline()

        try: 
            archivoItaliaAbierto.close()

        except IOError: 
            print("No se pudo cerrar correctamente el archivoItalia ")
        
###############################################################################################    

    try: 
        archivoEspañaAbierto = open(archivoEspaña, mode = 'rt')
    except IOError: 
        print("No se pudo abrir el archivoEspaña con exito ")

    else: 
        linea = archivoEspañaAbierto.readline()
        while linea: 
            print(linea.strip())
            linea = archivoEspañaAbierto.readline()

        try: 
            archivoEspañaAbierto.close()

        except IOError: 
            print("No se pudo cerrar correctamente el archivoEspaña ")
    
archivoArmenia, archivoItalia, archivoEspaña = guardarApellidos() 
mostrarApellidos(archivoArmenia, archivoItalia, archivoEspaña)