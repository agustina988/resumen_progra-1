# -> Metodos para usar con listas, (god)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# in, sirve para verificar si algo esta 'in' una lista 
lista = [4,1,2,3,4]
if 2 in lista: 
    print("esta perri ")

else:
    print("ese no esta perri ")

if 10 not in lista: 
    print("ese no esta perri ")
else: 
    print("esta perri ")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# insert(<pos>,<elemento>) inserta elementos en una posicion determinada en una lista 

lista.insert(1,8)

print(lista)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#pop (lista.pop(<posicion>)), si no se especifica nada borra el ultimo de la lista 
#pos = int(input("ingrese la pos que desea eliminar "))
#lista.pop(pos)
print(lista)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#remove (lista.remove(elemento)) elimina un elemento identificado por su valor, si hay mas de uno elimina el primero que encuentra empezando por 0 a len
#valor = int(input("Ingrese el valor que desea eliminar "))
#lista.remove(valor)
print(lista)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#index (lista.index(valor)) busca un valor y devuelve su posicion, si hay dos, muestra el primero desde el 0 a len
#valor = int(input("que valor desea averiguar su pos ")) 
#indice = lambda lista,valor: print(lista.index(valor))
#indice(lista,valor)
#index tambien permite especificar la region de busqueda 
# lista.index(inicio,valor,fin)
#print(lista.index(1,1,4))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#count (lista.count(elemento)) devuelve la cantidad de veces que esta repetido un elemento, cero si no lo encuentra 
contar = lambda lista, elemento: print(lista.count(elemento))
contar(lista,4) 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#clear, elimina todos los elementos de una lista (lista.clear())
lista2 = [125432,654125,56376]
#lista2.clear() 
print(lista2)
clearear = lambda listaCualquiera: print(listaCualquiera.clear())
clearear(lista2)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#metodo reverse, invierte el orden de los elementos de una lista 
lista.reverse()
print(lista)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#metodo sort (lista.sort()) ordena los valores de las listas, de manera default lo hace de menor a mayor 
#pero, escribiendo: lista.sort(reverse=True), ordena de mayor a menor, ojo con perder el paralelismo y las cadenas y simbolos se ordenan segun su valor en la tablas ASCII 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

list() #convierte cualquier secuencia en una lista 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#copy; copias la lista asi como te digo chango; 
lista2 = lista.copy() 
#genera listas independientes