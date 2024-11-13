# En Python, any() es una función incorporada que toma un iterable (como una lista, tupla, o generador) 
# y devuelve True si al menos uno de los elementos del iterable es True. 
# Si todos los elementos son False o el iterable está vacío, any() devuelve False.
# en las funciones lambda de Python no se pueden usar bucles for de manera explícita. 
# Sin embargo, puedes utilizar una expresión generadora dentro de la función lambda, 
# que es una forma concisa de generar secuencias.


is_oblong = lambda x: any(x == n * (n + 1) for n in range(1, int(x**0.5) + 1))

corroborar = is_oblong(20)

if corroborar == True: 
    print("es ")
else:
    print("Noes")
#------------------------------------------------------------------------------------------------------------v
is_triangular = lambda x: any(x == (n + (n+1)) for n in range(1, int(x**0.5) + 1))

corroborar = is_triangular(45)

if corroborar == True: 
    print("es")
else:
    print("Noes")