"""
    <nombre>=lambda<parametros>:<valor de retorno>
"""

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

multiplicar = lambda num1,num2 : print(num1 * num2)

multiplicar(5,5)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

concatenar = lambda str1, str2 : print (str1 + str2)

concatenar('holaa ','perdida')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

concatenarListas = lambda lista1, lista2 : print (lista1 + lista2)

lista1 = [1,2,3]
lista2= [4,5,6]

concatenarListas(lista1,lista2)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

eliminarPrimerValorListaConPop = lambda lista3 : print(lista3.pop(0)) # pop eliminar y devuelve, ojota ahi, por eso el print

lista3 = [99, 98, 97, 96]

eliminarPrimerValorListaConPop(lista3)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# eliminarPrimerValorListaConDel = lambda lista4 : del lista4[0], esto no se puede hacer, ya que del es una declaracion, no una funcion  o expresion, y las funciones lambda no admiten declaraciones (while, for, if else)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

eliminarPrimerValorListaConRemove = lambda lista4 : lista4.remove(777) # esto tampoco funciona, y aca te explico por que|
                                                                       #                                                |                             
lista4 = [777,778,779,780]                                             #                                                |
                                                                       #                                                |
pruebaFuncion = eliminarPrimerValorListaConRemove(lista4)              #                                                |
                                                                       #                                                |        
print(pruebaFuncion)                                                   #                                                |
                                                                       #                                                |         
                                                                       #                                                V
                                                                       # Si una función lambda contiene una expresión que no produce un valor (como una llamada a un método que no devuelve nada explícitamente), el valor de retorno de la lambda será None.

# pero si printeas la lista, se muestra correctamente, no es que no funcione, es que no tiene valor de retorno

print(lista4)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

raiz = lambda a,b: a **(1/b)

resultado = raiz(25,5)

print(resultado)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

mostrarMax = lambda lista5: print(max(lista5))

lista5 = [-432,1,32,5,5,2,32,765,873,23,312,5443,5443,5443]

mostrarMax(lista5)

mostrarMin = lambda lista5: print(min(lista5))

mostrarMin(lista5)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

sumarLista = lambda listaA: print(sum(listaA))

listaA = [5,4,2,1]

sumarLista(listaA)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

convertirEnLista = lambda argumento : print(list(argumento))

#donde argumento, puede ser, una cadena, un cojunto, una tupla o un rango 

#argumento = range(10)

argumento = 'maracatunga'

convertirEnLista(argumento)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

