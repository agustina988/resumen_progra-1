# Realizar una función que devuelva el resto de dos números enteros, utilizando res
# tas sucesivas. 

def restasSucesivas (n, m, resto = 0): 
    if resto == (n-m): 
        return resto 
    if n > m: 
        return restasSucesivas(n, m, resto +1)
    
    else: 
        return restasSucesivas(n, m, resto -1)
    
a =  restasSucesivas(10,5) 
print(a)

b = restasSucesivas(5,10)
print(b)