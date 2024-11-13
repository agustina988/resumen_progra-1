"""
Archivos de entrada: en ellos solo se pueden leer, pero no es posible grabar datos
Archivos de salida: en ellos solo se puede grabar, no es posible leer

Apertura - Open()
La apertura se realiza con la función open()
<var> = open(<nombre>,[,<modo>])
<var> es la variable que se usara para representar el archivo dentro del
programa.

Ejemplo: 
arch = open(“c:\nuevo\datos.txt”,”wt”) #da error por el \n
como se soluciona??
- Usar doble barra invertida. Cuando se vio cadena de caracteres
arch = open(“c:\\nuevo\\datos.txt”,”wt”)
- Una sola barra normal. La barra de dividir. Es mas propia de Linux.
Pero es aceptada en Windows
arch = open(“c:/nuevo/datos.txt”,”wt”)
- Declarar la cadena como cruda
arch = open(r“c:\nuevo\datos.txt”,”wt”)

El modo de apertura esta formado por uno o dos caracteres.
El primero es el modo básico de apertura y puede ser
r (read): abre el archivo en modo entrada, es decir para lectura solamente
w (write): abre el archivo en modo salida, es decir para grabación solamente
a (append): abre el archivo en modo salida, es decir para grabación solamente y agregado de registros

El segundo caracter del modo de apertura es el modificador t (texto).
Si se omite el modo de apertura por default se asume lectura y texto, es decir rt

Cierre de archivos:
Durante el cierre se revierte todo lo que se hizo en la apertura
Se clausuran los canales de comunicación con el dispositivo y se
liberan los buffers, grabando cualquier registro pendiente que pudiera
haber
TODO ARCHIVO SE DEBE CERRAR, se suele utilizar en finally para asegurar su ejecución.

Para cerrar un archivo se utiliza el método close() de la variable que representa al archivo:
archivo.close()

Metodos de grabacion:
- <arch>.write(<str>): graba <str> en el archivo. El salto de linea debe añadirse manualmente, porque este método no lo agrega
- <arch>.writelines(<lista>): graba una lista de cadenas. El salto de linea debe añadirse a cada elemento de la lista. Internamente tiene un ciclo.

Ejemplo:
1) Leer desde el teclado los datos correspondientes a los alumnos
de un curso (legajo y nombre) y grabarlos en un archivo csv
(comma-separated values, valores separados por comas).
Cada dato se separa con ; (punto y coma)
El fin de datos se indica ingresando un legajo -1
try:
    archivo=open("archivo.csv", "wt")
    bandera=True
    while bandera:
        legajo=int(input("ingrese el legajo del alumno. Ingrese -1 para terminar\n"))

        if legajo==-1:
            bandera=False
        else:
            nombre=input("ingrese el nombre\n")
            archivo.write(str(legajo)+','+nombre+'\n')
    print("archivo creado correctamente")

except OSError as mensaje:
    print("no se puede grabar el archivo: ", mensaje)
finally:
    try:
        archivo.close()
    except NameError:
        print("Error al cerrar")

<arch>.read([<n>]): lee un archivo de texto y devuelve una única cadena de caracteres. Este método lee el archivo entero, lo que puede ser muy peligroso con archivos grandes.
<arch>.readline([<n>]): lee una sola linea del archivo y la devuelve como valor de retorno, o una cadena vacía si no hay mas datos.
Es decir este método lee hasta que encuentra un \n

Ejemplo:
2) Leer el archivo de alumnos y mostrar por pantalla aquellos que tengan legajo menor a 10000
try:
    archivo=open("archivo.csv", "rt")
    linea=archivo.readline()

    while linea:
        legajo, nombre=linea.split(";")
        
        if int(legajo)<10000:
            print("legajo: ", legajo, "\t nombre: ", nombre)
        
        linea=archivo.readline()
finally:
    try:
        archivo.close()
    except NameError:
        print("error al cerrar")




"""






