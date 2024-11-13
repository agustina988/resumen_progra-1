# Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los
# próximos Juegos Panamericanos. Para eso encargó la realización de un programa
# que incluya las siguientes funciones:


# GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas
# disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una
# línea distinta. Ejemplo:
# <Deporte 1>
# <altura del atleta 1>
# <altura del atleta 2>
# < . . . > 
# <Deporte 2>
# <altura del atleta 1>
# <altura del atleta 2>
# < . . . >

# GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atle-
# tas, leyendo los datos del archivo generado en el paso anterior. La disciplina y el
# promedio deben grabarse en líneas diferentes. Ejemplo:
# <Deporte 1>
# <Promedio de alturas deporte 1>
# Deporte 2>
# <Promedio de alturas deporte 2>
# < . . . >

# mostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas
# superan la estatura promedio general. Obtener los datos del segundo archivo

def validarNumero():
    while True: 
        try: 
            numero = float(input("Ingrese la altura del atleta, -1 para finalizar "))
            break
        except ValueError: 
            print("por favor ingrese un numero ")

    return numero

def grabarAlturas(): 
    archivoAlturas = 'archivoAlturas.txt'
    try: 
        archivoAbierto = open(archivoAlturas, mode= 'wt')
    except IOError: 
        print("El archivo de alturas no se pudo abrir con exito ")
    else:

        disciplina = input("Ingrese la disciplina de los atletas -1 para finalizar: ")
        while disciplina != "-1": 
            
            disciplina = disciplina.upper()
            archivoAbierto.write("DISCIPLINA: " + disciplina + "\n")
            print("ingrese la altura de los atletas, -1 para finalizar con esta disciplina")
            numero = validarNumero()
            numeroAtleta = 0
            while numero != -1:
                numeroAtleta += 1
                numero = str(numero)
                linea = f"Altura del atleta {numeroAtleta}: "+ numero+ "\n"
                archivoAbierto.write(linea)
                numero = validarNumero()
            archivoAbierto.write("..." + "\n")  
            disciplina = input("Ingrese la siguiente disciplina, -1 para finalizar: ")
        
        try: 
            archivoAbierto.close()
        except IOError: 
            print("El archivo de alturas no se pudo cerrar con exito")

    return archivoAlturas


def grabarPromedio(archivoAlturas):
    archivoPromedios = "promedios.txt"
    cantLineas = 0
    alturasTotal = 0
    try: 
        archivoPromediosAbierto = open(archivoPromedios, mode = 'wt')
    except IOError: 
        print("No se pudo abrir el archivo de promedios ")
    else: 
        try:  
            archivoAbierto = open(archivoAlturas, mode = 'rt')
        except IOError: 
            print("El archivo no se pudo abrir con exito en la funcion grabar promedio ")
        else: 
            
            linea = archivoAbierto.readline()
            while linea: 
                    if "DISCIPLINA" in linea: 
                        archivoPromediosAbierto.write(linea)
                        palabra, deporte = linea.strip().split(":")
                        linea = archivoAbierto.readline()
                        continue
                    else:         
                        if "..." in linea:
                            promedio = alturasTotal / cantLineas
                            archivoPromediosAbierto.write("Promedio de alturas deporte"+ deporte+": "+ str(promedio) + "\n")
                            archivoPromediosAbierto.write(linea)
                            promedio = 0
                            cantLineas = 0
                            alturasTotal = 0
                            linea = archivoAbierto.readline()
                            continue
                        else:
                            texto, altura = linea.strip().split(":")
                            altura = float(altura)
                            cantLineas += 1
                            alturasTotal += altura
                       
                    linea = archivoAbierto.readline()
    try: 
        archivoAbierto.close()
    except IOError: 
        print("No se pudo cerrar el archivo de alturas ")
    try: 
        archivoPromediosAbierto.close()
    except IOError: 
        print("No se pudo cerrar el archivo de alturas promedio")

    return archivoPromedios

def mostrarMasAltos(archivoPromedios): 
    listaDisciplinas = []
    listaPromediosDisciplinas = []
    alturasDisciplina = 0
    atletasTotal = 0
    try: 
        archivoPromediosAbierto = open(archivoPromedios, mode = 'rt')
    except IOError: 
        print("El archivo promedios en la funcion mostrarMasAltos no se pudo abrir correctamente ")
    else: 
        linea = archivoPromediosAbierto.readline()
        while linea: 
            if "DISCIPLINA" in linea: 
                palabra, disciplina = linea.strip().split(":") 
                listaDisciplinas.append(disciplina)
                linea = archivoPromediosAbierto.readline()
                continue
            elif "..." in linea: 
                promedio = alturasDisciplina / atletasTotal
                listaPromediosDisciplinas.append(promedio)
                alturasDisciplina = 0
                atletasTotal = 0
                linea = archivoPromediosAbierto.readline()
                continue
            else: 
                texto, altura = linea.strip().split(":")
                alturasDisciplina += float(altura)
                atletasTotal += 1
                linea = archivoPromediosAbierto.readline()
    
    promediosTotal = 0
    cantidadDisciplinas = len(listaDisciplinas)
    for i in range(len(listaPromediosDisciplinas)):
        promediosTotal += listaPromediosDisciplinas[i]

    promedioAlturasDisciplinas = promediosTotal / cantidadDisciplinas
    for i in range(len(listaPromediosDisciplinas)): 
        if listaPromediosDisciplinas[i] > promedioAlturasDisciplinas: 
            print(f"La altura promedio del deporte{listaDisciplinas[i]} es mayor a la altura promedio de todas las disciplinas {promedioAlturasDisciplinas:.2f}")
                

archivoAlturas = grabarAlturas()
archivoPromedios = grabarPromedio(archivoAlturas)
mostrarMasAltos(archivoPromedios)