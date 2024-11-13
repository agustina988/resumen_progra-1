def convertirListaAnumero(listaNum, numeroEntero):
    numeroEntero = ''
    for i in range(len(listaNum)):
        numeroEntero += listaNum[i]

    return numeroEntero


def pasarRomano(valor, tipo, numeroRomano):
   
    listaUnidades = ['I','II','III','IV','V','VI','VII','VIII','IX'] #esto va de 1 a 9 
    listaDecenas = ['X','XX','XXX','XL','L','LX','LXX','LXXX','XC'] #contiene 10, 20, 30 40, 50, 60, 70, 80, 90
    listaCienes = ['C','CC','CCC','CD','D','DC','DCC','DCCC','CM'] #contiene 100, 200, 300, 400, 500, 600, 700, 800 ,900
    listaMiles = ['M', 'MM', 'MMM'] #mil 2mil 3mil

    if tipo == 'mil': 
        numeroRomano += listaMiles[valor -1]
    elif tipo == 'cien': 
        numeroRomano += listaCienes[valor -1]
    elif tipo == 'decena': 
        numeroRomano += listaDecenas[valor -1]
    else: 
        numeroRomano += listaUnidades[valor -1]
    
    return numeroRomano

def convertirNumeroAlista(numeroEntero):
  
    numeroEntero = str(numeroEntero)
    listaNum = []
    for i in range(len(numeroEntero)):
        listaNum.append(numeroEntero[i])

    if len(listaNum) == 4: 
        tipo = 'mil'
    elif len(listaNum) == 3: 
        tipo = 'cien'
    elif len(listaNum) == 2: 
        tipo = 'decena'
    else: 
        tipo = 'unidad'

    valor = ''
    valor += listaNum[0]
    valor = int(valor)

    listaNum.pop(0)

    while len(listaNum) > 0 and listaNum[0] == '0':
        listaNum.pop(0) 

    numeroEntero = convertirListaAnumero(listaNum, numeroEntero)

    return valor, tipo, numeroEntero


def main(): 
    numeroEntero = int(input("Ingrese el numero que desea convertir a romano "))
    numeroEntero = str(numeroEntero)
    numeroRomano = ''
    while len(numeroEntero) > 0: 
        valor, tipo, numeroEntero = convertirNumeroAlista(numeroEntero)
        numeroRomano = pasarRomano(valor,tipo,numeroRomano)
      
    print("su numero en romano es ",numeroRomano)

main()
