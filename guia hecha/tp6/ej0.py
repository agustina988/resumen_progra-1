def agregarAlumnos():    
    #un archivo puede dar error tanto en la apertura como en el cierre del mismo 
    try: 
        arch = open("/home/luciowo/progra_1/ejericios_guia/tp6/ej0/alumnos.txt", mode = 'w+t')
    except IOError: 
        print("no se pudo abrir el archivo")

    else: 
        try:        
            legajo = int(input("Ingrese legajo del alumno, -1 para finalizar "))
        except ValueError: 
            print("error, tenias que ingresar un entero")

        while legajo != -1: 
            nombre = str(input("Ingrese el nombre del alumno "))
            arch.write(str(legajo) + ";" + nombre + "\n")
            try: 
                legajo = int(input("Ingrese legajo del alumno, -1 para finalizar "))
            except ValueError: 
                print("tenias que ingresar un entero")
        try: 
            arch.close()
        except IOError: 
            print("El archivo no se pudo cerrar correctamente ")

    try: 
        arch = open("/home/luciowo/progra_1/ejericios_guia/tp6/ej0/alumnos.txt", mode = 'rt')
    except IOError: 
        print("Se produjo un error al abrir el archivo ")
    
    else: 
        try: 
            linea = arch.readline()
            while linea: 
                legajo, nombre = linea.split(";")
                if int(legajo) > 10000: 
                    print("Legajo: ",legajo,"Nombre: ",nombre)
                linea = arch.readline()

        finally: 
            try: 
                arch.close()
            except IOError: 
                print("no se pudo cerrar el archivo ")

agregarAlumnos()