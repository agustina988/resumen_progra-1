# La función de Ackermann A(m,n) se define de la siguiente forma:
# n+1 si m = 0
# A(m-1,1) si n = 0
# A(m-1,A(m,n-1)) de otro modo

# Imprimir un cuadro con los valores que adopta la función para valores de m entre 0 
# y 3 y de n entre 0 y 7.


def ackerman(m,n): 

    print("M: ",m, "N: ", n)

    if m == 0: 
        return n + 1
    elif m > 0 and n == 0: 
        return ackerman(m-1, n = 0) 
    
    elif m > 0 and n > 0: 
        return ackerman((m - 1), ackerman(m, n - 1))
    

habiaunavez = ackerman(25,1)

print(habiaunavez)