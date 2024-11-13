"""Realizar un programa para ingresar una frase
y mostrar un listado ordenado alfabeticamente
con las palabras que contiene, eliminando las
repetidas y añadiendo junto acda una
la cantidad de veces que se encontro"""

frase=input("ingrese una frase:")
palabras=frase.split()
dic={}
for palabra in palabras:
    if palabra not in dic:
        dic[palabra] = 1
    else:
        dic[palabra] = dic[palabra] + 1

claves=list(dic)
claves.sort()
for clave in claves:
    print(claves, "aparece: ", dic[clave], "veces")