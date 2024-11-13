"""excepciones:
-IndexError
-NameError
-ValueError
-ZeroDivisionError
-SyntaxError
-IndentationError
-TypeError
-AtributeError
-AssertionError
-IOError
-KeyError
-KeyboardInterrupt
-MemoryError
-ModuleNotFoundError
-RecursionError
-ArithmeticError

como funciona:

try:
    print(f"El promedio es: {suma/cant:4.2f}")
except ZeroDivisionError:
    print(f"La cantidad ingresada es 0")

try:
    Bloque de codigo que puede generar errores --> bloque protegido

except <excepcion a capturar>:
    bloque de codigo para tratar el error generado
"""

"""
import random
lista = [random.randint(1,20) for i in range(random.randint(5,10))]

try:
    posicion = int(input("ingrese posicion del elemento a mostrar: "))
except ValueError:
    print("no se ingreso un numero")
except IndexError:
    print("La lista no tiene tantos elementos")
"""

"""
Es posible capturar el mensaje de error asociado a la excepción generada utilizando la instrucción as
try:
    num = int("aaa")
except ValueError as msg:
    print(msg)
"""

#CLAUSULA ELSE:
"""
Luego de las cláusulas except, puede agregarse una cláusula else, cuyo bloque de código solo se ejecutará si el bloque protegido se ejecuto sin generar ningún error. 
try:
    porcentaje = (cant/total*100)
except ZeroDivisionError:
    print("No puede calcularse el porcentaje")
else:
    print(f"El porcentaje es {porcentaje:5.2f}%")
"""

#CLAUSULA FINALLY:
"""
Otra cláusula opcional es finally, cuyo bloque de código se ejecutará siempre, sin importar si hubo un problema durante la ejecución del bloque protegido.
try:
    porcentaje = (cant/total) * 100
except ZeroDivisionError:
    porcentaje = 0.0
finally:
    print(f"El porcentaje es {porcentaje:5.2f}%")
"""

#instruccion raise
"""
Permite provocar una excepción. Puede incluir o no el mensaje de error asociado.
raise ValueError ("Error de valor generado")

La instrucción raise puede utilizarse también para relanzar la última excepción producida.

try:
    num  = int("abc")
except ValueError as msg:
    print("No se pudo guardar el numero")
    print(msg)
    raise
    
"""

#instruccion assert:
"""
Se utiliza junto con una operación lógica, que en caso de ser falsa, genera una excepción del tipo AssertionError.

assert True 
assert 5>3
assert False

"""

#jerarquia de excepciones:
"""
Los tipos de excepciones están organizados jerárquicamente, de modo que distintas excepciones son a su vez de un mismo tipo más genérico.

try:
    capacidadTotal = int(input("Stock maximo: "))
    stockActual = int(input("Stock actual: "))
    if stockActual > capacidadTotal:
        raise OverflowError ("El stock supera la capacidad maxima")
    porcOcupado = stockActual *100 / capacidadTotal
    print(f"El almacen esta a un {porcOcupado:.2f}% de su capacidad")
except ValueError:
    print("El valor ingresado es incorrecto")
except ArithmeticError as msg:
    print(msg)

"""

#Excepciones personalizadas:
"""
Se pueden generar nuevos tipos de excepción para utilizar con la instrucción raise.

class EmptyListError(Exception):
    pass

def promedioLista(lista):
    if len(lista) == 0:
        raise EmptyListError("la lista esta vacia")
    else: 
        return sum(lista) / len(lista)

"""

