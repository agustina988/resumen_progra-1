# Desarrollar un programa para eliminar todos los comentarios de un programa es-
# crito en lenguaje Python. Tener en cuenta que los comentarios comienzan con el
# signo # (siempre que éste no se encuentre encerrado entre comillas simples o do-
# bles) y que también se considera comentario a las cadenas de documentación
# (docstrings).

   #

""" """

''' '''

def eliminarComentarios(archivo): 
    try: 
        archivoAbierto = open(archivo, mode = 'wt')
    except IOError: 
        print("El archivo no se pudo abrir con exito ")

    linea = archivoAbierto.readline()
    #while linea: 
