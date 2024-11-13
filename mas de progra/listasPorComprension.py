import random
# LISTAS POR COMPRENSION 
# lista = [expresion for variable in iterable ] 
# iterable -> coleccion de objetos (lista,tupla, etc)
#ejemplo 

#lista = [x ** 2 for x in range(5)]
#        ʌ expresion esto es lo que se agrega, lo que esta al inicio, y el elemento que se va a iterar en el bucle
#                   ʌ var, el for es cuantas veces
#                        ʌ iterable y el iterable es en que rango o en que secuencia iterable 
#print(lista)

#lista2 = [letra * 3 for letra in "ABC"]
#        ʌ expresion
#                   ʌ var
#                        ʌ iterable
#print(lista2)

#lista3 = [-4,-2,0,2,4]
#absolutos = [abs(elemento) for elemento in lista3]
#               ʌ expresion
#                               ʌ var
#                                           ʌ iterable
#print(absolutos)
 
#lista4 = [-4,-2,0,2,4]
#positivos = [elemento for elemento in lista4 if elemento >= 0] #tambien se pueden añadir condicionales if else 
#print(positivos)

#uso de else, se agregan los cuadrados de los numeros pares y los impares se agregan asi nomas
#lista5 = [num ** 2 if num %2 == 0 else num for num in lista5]

#uso de input 
#lista6 = [int(input("Ingresar un numero: ")) for i in range(10)]
#print(lista6)

n = int(input("cuantos elementos "))
lista7 = [random.randint(1,10)  for i in range(n)]
print(lista7)