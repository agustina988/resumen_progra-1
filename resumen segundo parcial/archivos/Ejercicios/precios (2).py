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

import random

def generarOriginal():
    codigos=[]
    try:
        archivo = open('precios.csv', 'wt')
        
        for i in range (5):
            cod=random.randint(1000,9999)
            while cod in codigos:
                cod=random.randint(1000,9999)
            codigos.append(cod)
            precio=round(random.uniform(100.5, 999.9),2)
            descripcion="PRODUCTO "+str(i+1)
            registro=str(cod)+";"+str(precio)+";"+descripcion
            archivo.write(registro + '\n')
            
        archivo.close()

        print("Archivo original 'precios.csv' generado correctamente.")
    except IOError:
        print("No se puede generar el archivo")
        
def actualizarPrecios(archivo_original, porcentaje):
    try:
        archivo = open(archivo_original, 'r')
        archivo_actualizado = open('Precios_actualizados.csv', 'w')
        
        total_productos = 0
        suma_precios = 0

        for linea in archivo:
            campos = linea.strip().split(';')
            codigo = campos[0]
            precio = float(campos[1])
            descripcion = campos[2]

            nuevo_precio = precio * (1 + porcentaje / 100)

            archivo_actualizado.write(f"{codigo};{nuevo_precio:.2f};{descripcion}" + '\n')
            total_productos += 1
            suma_precios += nuevo_precio

        archivo.close()
        archivo_actualizado.close()

        precio_promedio = suma_precios / total_productos

        print("Archivo 'Precios_actualizados.dat' generado correctamente.")
        print(f"Cantidad de productos comercializados: {total_productos}")
        print(f"Precio promedio con el incremento aplicado: {precio_promedio:.2f}")

    except FileNotFoundError:
        print(f"El archivo '{archivo_original}' no fue encontrado.")
    except ValueError:
        print("Error al procesar los precios. Asegúrate de que sean números válidos.")
    except Exception as e:
        print("Ocurrió un error inesperado:", str(e))


# Llamada a la función para generar el archivo original
generarOriginal()

# Llamada a la función para actualizar los precios
archivo_original = 'precios.csv'
while True:
    try:
        porcentaje_incremento = float(input("Ingrese el porcentaje de incremento: "))
        break
    except ValueError:
        print("Porcentaje inválido. Intente nuevamente.")

actualizarPrecios(archivo_original, porcentaje_incremento)
