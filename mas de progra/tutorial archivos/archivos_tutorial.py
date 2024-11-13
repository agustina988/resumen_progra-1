#INTRODUCCION

"""
Los tipos de actividades que se pueden realizar en el archivo abierto están controlados por los Modos de Acceso. 
Estos describen cómo se utilizará el archivo después de haber sido abierto.
Estos Modos de Acceso también especifican dónde debe ubicarse el controlador de archivo dentro del archivo. 
Similar a un puntero, un controlador de archivo indica dónde se deben leer o colocar los datos en el archivo.
"""
        
"""
(r) = solo lectura -> controlador al inicio del archivo; si no existe arroja error
(r+) = leer y escribir -> controlador al inicio del archivo; si no existe arroja error
(w) = solo escritura -> sobre-escribe y modifica los datos existentes del archivo -> controlador al incio de el archivo; si este no existe es creado 
(w+) = escribir y leer -> el texto del archivo es sobre-escrito; el controaldor se ubica al inicio del archivo 
(a) = solo agregar -> si el archivo no existe es creado; el controlador se ubica al final del archivo, los datos agergados se escriben al final de la archivo
(a+) = agregar y lee -> si el archivo no existe es creado; el controlador se ubica al final del archivo, los datos agergados se escriben al final de la archivo   
"""

#CREAR ARCHIVO

## Los archivos en python son creados con el metodo open() con una de las siguientes opciones -> 'x'(crear) o 'w'(escribir) 
## 'x' -> creara un archivo nuevo solo si no existe, de lo contrario devolvera error 
## 'w' -> creara un nuevo archivo de texto, sin importar si hay un archivo en la memoria con el nuevo nombre especificado, no devuelve error si encuentra un archivo con el mismo nombre, en su lugar, lo sobre-escribira

#crear un archivo de texto con la función de comando "x" 
file = open("myfile.txt", "x")

#creando un un texto con el el comando "w"
file = open("myfile.txt", "w")

#ESCRIBIR ARCHIVO

## Metodo write() -> esta funcion inserta la cadena en el archivo en una sola linea
file.write("Hello There\n")

## Metodo writelines() -> inserta varias cadenas al mismo tiempo, se crea una lista de elementos de cadena y luego cada cadena se agrega al final del archivo
file.writelines(["Hello world ", "You are welcome "])

#LEER ARCHIVO 

## Metodo read() -> esta funcion devuelve los bytes leidos como una cadena, si no se escpeficia una 'n' lee el archivo completo
print(f.read())

## Metodo readlines() -> esta funcion lee todas las lineas y las devuelve como elementos de cadena en una lista, uno por cada linea
print(f.readline())

#CERRAR ARCHIVO 

## Es una buena practica cerrar siempre el archivo cuando se ha terminado con el 
## La funcion close() -> cierra el archivo 
f = open('myfile.txt', 'r')
print(f.readline())
f.close()