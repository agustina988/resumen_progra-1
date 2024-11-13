#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#para acceder a un rango de items dentro de una lista necesitamos utilizar la tecnica de rebanadas o slicing 
#esto se hace o se puede hacer utilizando el operador ":"
#con este operador se puede  especificar, comienzo, fin y paso 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# lista= lista[2:7] ##esto modifica la lista original 

# lista = lista[-7:-2] #tambien se pueden especificar valores negativos con paso positivo de 1, esto invertido (-2:-7) -> no funcionaria ya que con paso positivo no se peude llegar de -2 a -7, necesitas paso negativo

# lista = lista[-2:-7:-1]  #aca, con el paso negativo especificado si es posible

# lista = lista[2:-5] #tambien se peuden combinar, de valor positivo a negativo paso positivo

# lista = lista[-5:2:-1] #si queres ir desde un valor negativo hasta uno positivo tenes que usar paso negativo

# el valor por omision del inicio es 0, el valor por omision de fin es el len de la lista y el de paso es 1  

# lista = lista[::-1] #invierte la lista

# lista[1:4] = ['a','b','c'] #---> o cualquier otro valor, reemplaza los valores especificados  

# lista[1:4] = ['a','b','c','d','e','f'] #---> por mas que haya mas valores de los que especificaste en el slicing, reemplza los especificados y agrega mas 

# lista[:0] = ['a','b','c'] # simplemente agrega elementos al inicio

# lista[len(lista):] = ['a','b','c'] # agrega elementos al final

# lista[1:1] = ['a','b','c'] # abre un hueco ahi y mete eso 

# lista[1:5] = [] #elimina reemplazando por vacio

# del lista[1:5] #tambien elimina a pleno

#   listaNueva = lista[:] #copia la lista, pero no se tienen dos listas, solo copia la referencia a la lista. por lo tanto la lista vieja y la nueva hacen referencia al mismo espacio de memoria

print(lista)
