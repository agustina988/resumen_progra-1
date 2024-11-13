cad1= "Lunes"
cad2 = "Martes"
frase1 = "Hoy es un hermoso dia para programar" #ES CASE SENSITIVE -> DISTINGUE MAYUSCULAS

# OPERADORES 

# las cadenas de caracteres se pueden concatenar +

nombre = input("ingrese su nombre: ")
saludo = "hola " + nombre
print(saludo)

# replicar *

asteriscos = "*" * 10 
print(asteriscos)

# buscar con in  

cad = "Martes"
if "te" in cad: 
    print("se encuentra")

else: 
    print("no se encuentra")

#comparar == 

pais = input("Ingrese su pais de nacimiento ")
if pais == "Argnetina": 
    print("La nacionalidad es Argentino")
else:
    print("La nacionalidad NO es Argentino")

# para concatenar un numero a una cadena, primero se debe convertir a cadena str(valor)

edad = 25
mensaje = "la edad es " + str(edad)

altura = 1.75
mensaje2 = "la altura es " + str(altura)

# se puede iterar 

cad = "Hoy es viernes"
for letra in cad: 
    print(letra)

# se puede acceder usando subindices 
# NO SE PUEDE MODIFICAR USANDO SUB INDICES -> LAS CADENAS SON INMUTABLES

cadena = "el perro roude"
print(cadena[0])

# se puede manipular usando rebanadas (slicing)
# en el slicing se llega hasta el valor de fin - 1 <--
cad = "Martes"
print(cad[0:3])


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# funciones con cadenas de caracteres 

print(len(cad))
print(max(cad) ,min(cad))

# metodos 

cad = "somofabich"

print(cad.count("o")) #contar elemento 

print(cad.index("fabi")) #valor de inicio de la subcadena buscada

cad = "hoy presento el tp de progra, que paja!"

cad = cad.replace('presento', 'me cojo') # reemplazar valores de la cadena, primero se ingresa lo que se va a remplazar luego el remplzao 

print(cad)

# y si tenes mas de una coincidencia? 

cad = "el perro perro roude"

cad = cad.replace('perro', 'somofabich') # -> remplaza todas las coincidencias 

print(cad)


#----------------------------------------------------------------------------------------------------------------------------------------------------
## METODOS IS 

cad = "Python"
print(cad.isalpha())

cad = "Python3"
print(cad.isalpha())#-> retorna true si todos los caracteres de la cadena son del alfabeto(solo letras(ni espacios ni otros caracteres))

print(cad.isdigit())#-> retorna true si todos los elementos de la cadena son numeros

print(cad.isalnum())#-> retorna true si los elementos de la cadena son letras o numeros (ni espacios ni otros caracteres especiales)

print(cad.isupper())#-> retorna true si todos los caracteres de la cadena estan en mayuscula

print(cad.islower())#-> retorna true si todos los caracteres de la cadena estan en minusculas 


#----------------------------------------------------------------------------------------------------------------------------------------------------


print(cad.upper())#-> devuelve una cadena convertida a mayusculas, ignora los caracteres no alfabeticos

print(cad.lower())#-> devuelve una cadena convertida a minusculas, ignora los caracteres no alfabeticos

print(cad.capitalize())#-> devuelve una cadena convirtiendo a mayuscula solo el primer caracter de la primer palabra

print(cad.title())# -> devuelve una cadena convertida a mayuscula el primer caracter de cada palabra y el resto en minusculas


#----------------------------------------------------------------------------------------------------------------------------------------------------
#METODO SPLIT 

#subdivide cadenas buscando espacios en blanco 
cad = input("ingrese una entidad: ")
listaPalabras = cad.split()
sigla = ""
for palabra in listaPalabras: 
    sigla = sigla + palabra[0]
sigla = sigla.upper()
print(sigla)


#----------------------------------------------------------------------------------------------------------------------------------------------------


# <cadena>.center(<ancho>,[relleno])
# osea, alarga la cadena, agregando los elementos que vos le digas, al ancho que vos le digas
# si le pasas un ancho menor al de la palabra, directamente no hace nada 
# si el numero que pones de ancho es impar, agrega mas del lado izquierod (inicio)
cad1 = "hola"
cad2 = cad1.center(30,'-') 
print(cad2)
 

#ljust 
# deja la palabra del lado izquierdo y agrega al derecho
cad1 = "Hola"           
cad2 = cad1.ljust(10,'-') 


#rjust
#lo mismo pero al reves
cad1 = "hola"
cad2 = cad1.rjust(10,'-') 


#----------------------------------------------------------------------------------------------------------------------------------------------------


#zfill
#si lo pisas no funciona, tenes que crear una variable nueva
#zfill agrega ceros a la izquierda hasta que la cadena tenga la longitud especificada en el parentesis
n = 3 
cad = str(n).zfill(5)
print(cad)
cad = "10"
lol = cad.zfill(10) 
print(lol) 


#----------------------------------------------------------------------------------------------------------------------------------------------------
# STRIP 

#lstrip <cadena>.lstrip(<str>)
#devuelve una cadena sin los caracteres indicados en str al inicio de la 
#es como que 'estripa' el caracter que le indiques, en este caso a la izuquierda (left)
cad = "---Hola-Mundo-----"
cad = cad.lstrip("-")
print(cad)


# <cadena>.rstrip(<str>)
#devuelve una cadena sin los caracteres ndicados en str al final de la cadena
cad = "---Hola-Mundo---" #lo mismo que la anterior pero del lado derecho
cad = cad.rstrip("-")
print(cad)


#<cadena>.strip(<str>) 
#devuelve una cadena sin los caracteres indicados en str al inicio y al final de la cadena 
cad = "---Hola-Mundo---"
cad = cad.strip("-")
print(cad) #en este caso se conservaria el '-' del medio ya que solo afecta al inicio y fin de la cadena 


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FORMATO 

# %formato
# <str>.format(<datos>)
legajo = 11212
nombre = "Maria"
nota = 10


#Formato con % disponible a partir de python 2.6
print("legajo: %d Nombre: %d, Nota: %d" %(legajo,nombre,nota))


#Metodo format ()
print("Legajo:{} Nombre:{} Nota:{}".format(legajo,nombre,nota))


#f string PEP498, el prefijo f te permite dar formato a una cadena de caracteres, por ejemplo
print(f"Legajo: {legajo} Nombre: {nombre} Nota: {nota}")


 #--------------------------------------------------------------------------------------------------------------------------------------------------