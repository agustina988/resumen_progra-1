# 4. Desarrollar una función que devuelva el producto de dos números enteros por su
# mas sucesivas.

def sumasSucesivas(n,m,producto = 0): 
    if producto == (n * m): 
        return producto 
    return sumasSucesivas(n,m, producto + 1)

lol = sumasSucesivas(5,5)
print(lol)