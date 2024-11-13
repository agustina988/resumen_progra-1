#Este programa muestra cómo escribir datos en un archivo de texto.This 

file = open("myfile.txt","w")
L = ["este podria ser mi programa de tareas \n", "pero no se como seria la implementacion \n", "me cago en mis muertos \n"]


file.write("bienvenido lucio \n")
file.writelines(L)
file.close()

# Usar close() para cambiar los modos de acceso a archivos

f = open('myfile.txt', 'r')

print(f.read())