"""
Son estructuras de datos para relacionar Clave - Valor
También se los conoce como arreglos asociativos o tablas de Hash

No son secuencias, por lo tanto no están ordenados.
No se puede utilizar índice para acceder a elementos
Las rebanadas No son aplicables a los diccionarios (carecen de orden interno)
Los elementos se acceden mediante la clave.

Cada elemento de un diccionario se representa mediante dos valores clave-valor
Se crean entre llaves y separando por comas
edades={"Juan":23, "maria":18, "marcelo":30}
print(edades)

Las claves deben pertenecer a un tipo inmutable (números, cadenas, tuplas)
Los valores asociados a cada clave pueden ser de cualquier tipo incluso listas u otro diccionario
colores={"rojo":[255,0,0], "verde":[0,255,0], "azul":[0,0,255]}
print(colores)

Los diccionarios inicializados, suelen escribirse con un formato más claro y legible, colocando una dupla debajo de la otra
colores={"rojo":[255,0,0],
         "verde":[0,255,0], 
         "azul":[0,0,255]
         }
print(colores)

Acceder a un valor de una clave:
edades={"Juan":23, "maria":18, "marcelo":30}
print(edades["marcelo"])

Un mismo valor puede estar asociado a más de una clave:
edades={"Juan":23, "maria":18, "marcelo":30, "pedro":23}

Las claves deben ser únicas (No admite claves duplicadas)
edades={"Juan":23, "maria":18, "marcelo":30, "pedro":23, "maria":25} #NO VA
edades={"Juan":23, "maria":18, "marcelo":30, "pedro":23} #SI VA

Asignar un valor a una clave reemplaza el valor existente o crea una clave nueva, dependiendo si existe o no previamente la clave.
colores={"rojo":[255,0,0],
         "verde":[0,255,0], 
         "azul":[0,0,255]
         }

colores["gris"]=[128,128,128]

No es posible acceder a una clave a través de su valor Tratar de acceder a un elemento con una clave inexistente provoca una excepción KeyError
colores={"rojo":[255,0,0],
         "verde":[0,255,0], 
         "azul":[0,0,255]
         }

print(colores["amarrillo"])

Se puede evaluar si una clave existe con el operador in ( o con el operador not in)
if "amarillo" in colores:
    print(colores["amarillo"])
else:
    print("No existe el color amarillo")

Se puede utilizar el método get(<clave>) Retorna el valor asociado a la clave None si no existe la clave
colores={"rojo":[255,0,0],
         "verde":[0,255,0], 
         "azul":[0,0,255]
         }

print(colores.get("rojo")) #[255,0,0]

El método get(<clave>, valor) Admite un segundo parámetro que será devuelto si No existe la clave
colores={"rojo":[255,0,0],
         "verde":[0,255,0], 
         "azul":[0,0,255]
         }

print(colores.get("amarillo")) #None

colores={"rojo":[255,0,0],
         "verde":[0,255,0], 
         "azul":[0,0,255]
         }

print(colores.get("amarillo", "no existe")) #no existe

El método items(<diccionario>) Retorna una lista de tuplas con clave,valor
colores={"rojo":[255,0,0],
         "verde":[0,255,0], 
         "azul":[0,0,255]
         }

for color,rgb in colores.items():
    print(color, "->", rgb)

#consola:
#rojo -> [255,0,0]
#verde -> [0,255,0]
#azul -> [0,0,255]

Podemos recorrer un diccionario:
for clave in diccionario:
    print("clave:", clave, "valor: ", diccionario[clave])
for color in colores:
    print(color, "->", colores[color])
    
#consola:
#rojo -> [255,0,0]
#verde -> [0,255,0]
#azul -> [0,0,255]

El método keys(<diccionario>) Retorna una vista de todas las claves (iterable) y actúa como un conjunto
claves=colores.keys()
print(claves)
#consola:
#dict_keys(['rojo', 'verdes', 'azul'])

El método values(<diccionario>) Retorna una lista con todos los valores
valores=edades.values()
print(valores)
#consola:
#dict_values([23,25,30,23])

Para eliminar un elemento se puede utilizar la instrucción del
colores={"rojo":[255,0,0],
         "verde":[0,255,0], 
         "azul":[0,0,255]
         }
del colores["rojo"]
print(colores) #Retorna excepción KeyError si no existe la clave

#consola:
#{'verde': [0,255,0], 'azul': [0,0,255]}

La instrucción del Permite eliminar Todo el diccionario
colores={"rojo":[255,0,0],
         "verde":[0,255,0], 
         "azul":[0,0,255]
         }
del colores
print(colores) #NameError: name 'colores' is not defined

El método clear() Permite vaciar el contenido del diccionario
colores={"rojo":[255,0,0],
         "verde":[0,255,0], 
         "azul":[0,0,255]
         }
colores.clear()
print(colores) #{}

Se puede utilizar la función len(<dic>)
colores={"rojo":[255,0,0],
         "verde":[0,255,0], 
         "azul":[0,0,255]
         }
print(len(colores)) #3

Iterar por un diccionario se obtienen las claves. Convertir un diccionario a una lista, se obtienen todas las claves en una nueva lista
colores={"rojo":[255,0,0],
         "verde":[0,255,0], 
         "azul":[0,0,255]
         }
claves=list(colores)
print(claves) #['rojo', 'verde', 'azul']

"""








