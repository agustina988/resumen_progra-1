"""
Realizar un programa que permite actualizar una lista de precios
en forma masiva, ingresando un porcentaje de incremento.
Debera:
1- Mediante una funcion generarOriginal crear el archivo original se
    llama precios.csv y fue generado utilizando el siguiente diseno de registro:
    • Código (entero de 4 digitos)
    • Precio (valor real)
    • Descripción
    Se dispone un registro por producto, y los campos son separados por ;
2- Desarrollar la funcion actualizarPrecios que recibe el nombre del archivo
    original y el porcentaje de incremento, y se encarga de recorrer el archivo y actualizar
    los precios correspondientes. Para ello se creara el archivo Precios_actualizados.csv.
3- Al finalizar informar la cantidad de productos comercializados, y el precio promedio
   con el incremento aplicado
RESOLVER VALIDANDO EL INGRESO DE LOS DATOS,  y MANEJANDO
CORRECTAMENTE LAS EXCEPCIONES
"""

#    1234;78000;"desc"
import random

def generarOriginal():
    codigos = []
    precios = []
    descripciones = []
    archivo = "precios.csv"
    try:
        archivoAbierto = open(archivo, mode = 'wt')
    except IOError: 
        print("el archivo no se pudo abrir correctamente ")

    else:
        for i in range(100): 
            codigo = random.randint(1000, 9999)
            if codigo not in codigos:
                codigos.append(codigo)
                precio = random.randint(10000, 100000)
                if precio not in precios: 
                    precios.append(precio)
                    descripcion = random.randint(100,999)
                    if descripcion not in descripciones:
                        descripciones.append(descripcion)
                        archivoAbierto.write(str(codigo) + ";" + str(precio) + ";DESC" + str(descripcion) + "\n")
        try: 
            archivoAbierto.close()
        except IOError: 
            print("El archivo no se pudo cerrar con exito en la funcion generar original")

    return archivo

def actualizarPrecios(archivo, porcentaje):
    try:   
        archivoAbierto = open(archivo, mode = 'rt')
    except IOError: 
        print("El archivo no se pudo abrir con exito en la funcion actualizar precios ")
    else:
            
        archivoActualizado = "precios_actualizados.csv"
        try:
            archivoActualizadoAbierto = open(archivoActualizado, mode = 'wt')
        except IOError: 
            print("El archivo actualizado no se pudo abrir correctamente ")
        else:
                
            linea = archivoAbierto.readline()
            while linea: 
                lin = linea.strip().split(";")
                cod=lin[0]
                precio = int(lin[1]) * porcentaje
                desc = lin[2]
                archivoActualizadoAbierto.write(cod + ";" + str(precio) + ";" + desc + "\n")
                linea = archivoAbierto.readline()
            try: 
                archivoActualizadoAbierto.close()
            except IOError: 
                print("El archivo actualizado no se pudo cerrar con exito ")

    return archivoActualizado

def informes(archivoActualizado): 
    productos = 0
    precioTotal = 0
    try:
        archivoActualizadoAbierto = open(archivoActualizado, mode = 'rt')
    except IOError: 
        print("El archivo actualizado no se pudo abrir con exito en la funcion informes")
    else: 
        linea = archivoActualizadoAbierto.readline()
        while linea:
            campos = linea.strip().split(";")
            print(campos)
            #codigo = campos[0]
            precio = float(campos[1])
            #descripcion = campos[2]
            productos += 1
            precioTotal +=precio
            linea = archivoActualizadoAbierto.readline()
        try: 
            archivoActualizadoAbierto.close()
        except IOError: 
            print("No se pudo cerrar correctamente el archivo actualizado en la funcion informes")
        print("cantidad de productos comercializados: ", productos)
        print("ganancia promedio obtenida con porcentaje aplicado: ", (precioTotal / productos))
    return productos, precioTotal

archivo = generarOriginal()
archivoActualizado = actualizarPrecios(archivo,0.90)
productos, precioTotal = informes(archivoActualizado)
print(productos, precioTotal)