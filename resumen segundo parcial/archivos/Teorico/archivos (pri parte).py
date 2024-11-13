"""
Archivos:
Conjunto de elementos llamados registros
TODOS del mismo tipo de dato almacenado en un
dispositivo auxiliar para preservar la información en
el tiempo (discos, cintas, memorias NO volátil)

Según el contenido de los registros:
Archivos de texto
Archivos binario

Los datos se almacenan como
cadenas de caracteres
No tienen formato: texto plano
Pueden ser creados, visualizados o modificados por
cualquier editor de texto:
- block de notas de Windows
- IDLE de Python

El delimintador que se utiliza es \n «secuecia de escape» representa un salto de línea
print("lunes \nmartes \nmiercoles")
#consola:
#lunes 
#martes 
#miercoles

Apertura:
TODO ARCHIVO DEBE SER ABIERTO PREVIO A SER UTILIZADO
<variable> = open(file, mode='r')
arch = open(“datos.txt”)
arch = open(“datos.txt”, mode=‘rt’)
arch = open(“c:\\nuevo\\datos.txt”, mode=‘rt’)
arch = open(r“c:\nuevo\datos.txt”, mode=‘rt’)

APERTURA <variable> = open(file, mode='r')
mode: indica el modo de apertura del archivo, por
default es modo lectura de un archivo de texto
Primer Caracter:
w: escritura
r: lectura
Segundo Caracter:
t: texto
b: binario

Si no se logra abrir el archivo produce un error del tipo IOError
try:
    #abre un archivo de texto en modo escritura:
    arch=open(r"d:\alumnos.txt", "wt")
except OSError as msg:
    print("error ", msg) #error  [Errno 2] No such file or directory: 'd:\\alumnos.txt'

Cierre:
TODO ARCHIVO SE DEBE CERRAR, se suele utilizar
En finally para asegurar su ejecución
<arch>.close()
try:
    #abre un archivo de texto en modo escritura:
    arch=open(r"d:\alumnos.txt", "wt")
except OSError as msg:
    print("error ", msg)
else: 
    #cierra el archivo de texto
    arch.close()

proceso: escritura
Realizar grabaciones sobre el archivo.
El salto de línea se debe agregar a la cadena
<arch>.write(<cadena>)
Graba la <cadena> en el archivo.
SE DEBE AGREGAR EL SALTO DE LINEA
Ejemplo:

Proceso: lectura
Realizar lecturas sobre el archivo existente.
<cadena>=<arch>.readline()
Lee y retorna una sola línea del archivo.
Retorna una cadena vacía si no hay más líneas.
Ejemplo:

Un archivo es iterable. Podemos utilizar
For … in para recorrer un archivo
Ejemplo:


"""


