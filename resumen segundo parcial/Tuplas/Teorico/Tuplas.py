"""
Son similares a las listas
Sus elementos son inmutables

Intentar modificar una tupla provoca un error: TypeError


Para crear una tupla, se utiliza () y , () son opcionales
semana=("lunes", "martes", "miercoles", "jueves", "viernes")
semana="Lunes", "martes", "miercoles", "jueves", "viernes"


#Tupla vacia:
dias=()

#Para crear una tupla con un elemento se debe agregar coma:
dias=("Lunes",)

#En una tupla se pueden combinar distintos tipos de datos:
primavera=(21,"septiembre")
invierno(21,"junio")

#Tuplas de Tuplas:
primavera=(21,"septiembre")
invierno(21,"junio")
estaciones=(primavera, invierno)
print(estaciones)

#Podemos: utilizar el operador + para agregar elementos a la tupla
fecha=()
fecha=fecha + (25,)
fecha+=("enero",)
fecha+=(2009,)
print(fecha)

#Podemos: acceder a cada elemento con subíndice
fecha[0]
fecha[1]
fecha[2]

#Podemos utilizar el operador * para replicar los elementos
binario=(0,1)*3
print(binario) #muestra (0,1,0,1,0,1)

#Ejemplo: Tupla Alumnos con nombre y Fecha de nacimiento como tupla:
fecha=()
fecha=fecha + (25,)
fecha+=("enero",)
fecha+=(2009,)

print(fecha)

alumno="lautaro"
alumno="lautaro",
alumno=alumno + (fecha,)
print(alumno)

print(alumno[0]) #lautaro
print(alumno[1]) #25,'enero', 2009
print(alumno[1][0]) #25
print(alumno[1][1]) #enero
print(alumno[1][2]) #2009

#se puede iterar con un ciclo:
semana=("lunes", "martes", "miercoles", "jueves", "viernes")
for dia in semana:
    print(dia) 
#print:
#lunes
#martes
#miercoles
#jueves
#viernes

#se pueden utilizar rebanadas:
semana=("lunes", "martes", "miercoles", "jueves", "viernes")
print(semana[1:3]) #('martes', 'miercoles')

EXPLICACION:
Aquí se usa slicing para extraer una porción de la tupla semana. La notación [1:3] selecciona los elementos desde el índice 1 hasta el índice 3 (sin incluir este último).

semana[1] es "martes"
semana[2] es "miercoles"
Entonces, semana[1:3] devuelve la sub-tupla ("martes", "miercoles").


findeLargo=semana[len(semana)-1:] + ("sabado", "domingo")
print(findeLargo) #('viernes', 'sabado', 'domingo')}

EXPLICACION:
semana[len(semana)-1:]: len(semana) devuelve 5, ya que la tupla semana tiene 5 elementos.

len(semana) - 1 es 4, por lo que semana[4:] selecciona el último elemento de semana, es decir, ("viernes",).
Suma de tuplas: Se suma ("viernes",) con ("sabado", "domingo"), lo cual resulta en la nueva tupla ('viernes', 'sabado', 'domingo').

Entonces, el resultado de findeLargo es ('viernes', 'sabado', 'domingo').

#Funciones, operadores y metodos:
Funciones: len(), max(), min(), sum()
Operador: * + in
Métodos: index(), count()

#empaquetado:
Es el proceso por el cual, una serie de valores simples se convierten en una tupla
dia=22
mes=10
año=2019
fecha=(dia, mes, año)
print(fecha) #(22,10,2019)

#Es el proceso por el cual, una tupla se asigna a una serie de variables simples:
fecha=(25,'enero',2009)
dia, mes, año=fecha 
print(dia, mes, año)



"""








