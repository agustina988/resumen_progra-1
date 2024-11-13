def centrarCadena(cadena): 
    cad = cadena.center(150,'-')
    print(cad)

cad = ''
for i in range(80): 
    cad += 'A'

centrarCadena(cad)