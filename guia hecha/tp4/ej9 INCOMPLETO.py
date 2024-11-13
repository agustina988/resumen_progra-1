#no se como hacer bro


import re 

cadena = "hice, un! don. de los defectos como dumbo"

def ordenarPalabrasLongitud(cadena): 
    lista1 = cadena.split()
    lista2 = []
    lista3 = []

    patron = "(\! \? \. \; \, \: \" \' \« \» \¿ \¡ \( \) \-)"

    for i in range(len(lista1)):
        lista2.append(lista1[i])

    for i in range(len(lista2)): 
        if '!' in lista2[i] or '?' in lista2[i] or '.' in lista2[i] or ',' in lista2[i] or ';' in lista2[i] or ':' in lista2[i] or '-' in lista2[i] or '—' in lista2[i] or '(' in lista2[i] or ')' in lista2[i] or '"' in lista2[i] or "'" in lista2[i] or '«' in lista2[i] or '»' in lista2[i] or '...' in lista2[i] or '¿' in lista2[i] or '¡' in lista2[i]:
            lista2[i] = re.sub(r'[!?.;,:"\'«»¿¡()-]', '', lista2[i])


    
    for i in range(len(lista2)): 
        if '!' in lista2[i][0] or '?' in lista2[i][0] or '.' in lista2[i][0] or ',' in lista2[i][0] or ';' in lista2[i][0] or ':' in lista2[i][0] or '-' in lista2[i][0] or '—' in lista2[i][0] or '(' in lista2[i][0] or ')' in lista2[i][0] or '"' in lista2[i][0] or "'" in lista2[i][0] or '«' in lista2[i][0] or '»' in lista2[i][0] or '...' in lista2[i][0] or '¿' in lista2[i][0] or '¡' in lista2[i][0]:
            lista3.append(lista2[i])
        
    print("lista 3 ", lista3)
        #elif '!' in lista2[i][len(lista2)]


    desordenada = True
    while desordenada == True:
        desordenada = False

        for i in range(len(lista2)-1):
            if len(lista2[i]) < len(lista2[i+1]): 
                aux = lista2[i]
                lista2[i] = lista2[i +1]
                lista2[i +1] = aux
                desordenada = True



    print(lista1, lista2)

check = ordenarPalabrasLongitud(cadena)
