"""
Es una colección de elementos sin orden y sin duplicados.
Es una colección de elementos sin orden y sin duplicados
No tienen orden interno : NO es una secuencia
Pueden contener elementos de distinto tipo

#Para crear un conjunto, se utiliza {} y ,
paises={"argentina", "brasil", "chile", "uruguay"}

#funciones, operadores y metodos:
Funciones: len(), max(), min(), sum()
Operador: in, not in, matemáticos
Métodos: add, remove, discard, clear, issubset

# & interseccion:
a= {1,2,3,4,5,6,7}
b={2,4,6,8,10}
c=a&b
print(c) #{2, 4, 6}

# | union:
a={1,2,3,4,5,6,7}
b={2,4,6,8,10}
c=a|b
print(c) #{1, 2, 3, 4, 5, 6, 7, 8, 10}

# - resta:
a={1,2,3,4,5,6,7}
b={2,4,6,8,10}
c=a-b
print(c) #{1, 3, 5, 7}

# ^ diferencia simetrica:
a={1,2,3,4,5,6,7}
b={2,4,6,8,10}
c=a^b
print(c) #{1, 3, 5, 7, 8, 10}

# add(<elemento>): agrega un elemento al conjunto
paises={"argentina", "brasil", "chile", "uruguay"}
paises.add("paraguay")
print(paises) #{'paraguay', 'brasil', 'chile', 'argentina', 'uruguay'}

# remove(<elemento>): elimina el elemento del conjunto, provoca una excepcion (KeyError) si no esta presente
paises = {"argentina", "brasil", "chile", "uruguay"}
print(paises)
paises.remove("brasil")
print(paises)

# discard(<elemento>): elimina el elemento del conjunto. no provoca error si no se encuentra en el conjunto
paises = {"argentina", "brasil", "chile", "uruguay"}
print(paises)
paises.discard("brasil")
print(paises)

# clear(): elimina TODOS los elementos del conjunto
paises = {"argentina", "brasil", "chile", "uruguay"}
print(paises)
paises.clear()
print("no hay paises: ", paises)

# issubset(<conjunto>): retorna TRUE si <conjunto> esta incluido en el conjunto
conjunto={3,4,5}
if conjunto.issubset({2,3,4,5,6}):
    print("incluido")
else:
    print("no incluido")

convertidor tipo de datos:
set(<iterable>) :convierte a conjunto
list(<iterable>) :convierte a lista
tuple(<iterable>):convierte a tupla

#tupla a conjunto:
a=set((2,3,2))
print(a) #{2, 3}

#conjuto a tupla:
b=tuple({2,3,4})
print(b) #(2, 3, 4)

#tupla a lista:
fecha=list((2,10,2019))
print(fecha) #[2, 10, 2019]

#lista a tupla:
fecha=tuple([2,10,2019])
print(fecha) #(2, 10, 2019)

#lista a conjunto:
conjunto=set([2,2,4,5,6,4])
print(conjunto) #{2, 4, 5, 6}

#conjunto a lista:
lista=list({2,5,7})
print(lista) #[2, 5, 7]


"""

