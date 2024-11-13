import random

def cargarNaranjas(naranjasTotales): 
    naranjasComer = 0
    naranjasJugo = 0
    cajonesNaranjaComer = 0
    cajonesNaranjaJugo = 0
    naranjasComerSobrantes = 0
    naranjasJugoSobrantes = 0
    naranjasRestantes = naranjasTotales
    contadorCienComer = 0
    contadorCienJugo = 0
    pesoNaranjasComer = 0
    pesoNaranjasJugo = 0

    listaPesoCajonesNaranjasComer = []
    listaPesoCajonesNaranjasJugo = []

    for i in range(naranjasTotales): 

        if naranjasRestantes > 100:
            naranjaAux = random.randint(150,350)

            if naranjaAux >= 200 and naranjaAux <= 300:
                naranjasComer += 1
                contadorCienComer += 1
                pesoNaranjasComer += naranjaAux

                if contadorCienComer == 100: 
                    cajonesNaranjaComer += 1
                    contadorCienComer = 0 
                    listaPesoCajonesNaranjasComer.append(pesoNaranjasComer)
                    pesoNaranjasComer = 0
            else: 
                naranjasJugo += 1
                contadorCienJugo += 1
                pesoNaranjasJugo += naranjaAux

                if contadorCienJugo == 100:
                    cajonesNaranjaJugo += 1
                    contadorCienJugo = 0
                    listaPesoCajonesNaranjasJugo.append(pesoNaranjasJugo)
                    pesoNaranjasJugo = 0
                    

        else:
            naranjaAux = random.randint(150,350)

            if naranjaAux >= 200 and naranjaAux <= 300:
                naranjasComerSobrantes += 1 

            else: 
                naranjasJugoSobrantes += 1
        
        naranjasRestantes -= 1

    print("Cantidad total de naranjas ", naranjasTotales)

    print("Cantidad total de naranjas comer ", naranjasComer)

    print("Cantidad total de naranjas jugo ", naranjasJugo)

    print("Cantidad total de cajones de naranja comer ", cajonesNaranjaComer)
    
    print("Cantidad total de cajones de naranja jugo ", cajonesNaranjaJugo)
            
    print("Cantidad total de naranjas comer restantes", naranjasComerSobrantes)
    
    print("Cantidad total de naranjas jugo restantes ", naranjasJugoSobrantes)

    return contabilizarCamiones(cajonesNaranjaComer, cajonesNaranjaJugo,listaPesoCajonesNaranjasComer,listaPesoCajonesNaranjasJugo)

def ingresarNaranjas(): 
    naranjasTotales = int(input("Ingrese la cantidad total de naranjas de la cosecha "))
    while naranjasTotales < 1:
        naranjasTotales = int(input("Por favor ingrese una cantidad total de naranjas valida (> 1) "))
    
    return cargarNaranjas(naranjasTotales)

def contabilizarCamiones(cajonesNaranjaComer, cajonesNaranjaJugo,listaPesoCajonesNaranjasComer,listaPesoCajonesNaranjasJugo): 
    peso = 0
    camiones = 0
    pesoTotal = 0
    camionNodespachado = 0
    for j in range(len(listaPesoCajonesNaranjasComer) -1): 
        peso += listaPesoCajonesNaranjasComer[j]
        peso += listaPesoCajonesNaranjasComer[j]
        pesoTotal += listaPesoCajonesNaranjasComer[j]
        pesoTotal += listaPesoCajonesNaranjasComer[j]
        
        if peso >= 500000:
            camiones += 1
            peso = 0
    if peso > 400000: 
        camiones += 1 
    else: 
        camionNodespachado += 1
    print("Se necesitaron ", camiones, " camionespara transportar ", pesoTotal,"Gr/",(pesoTotal // 1000),"Kg" ,"de naranjas para jugo y para comer,", camionNodespachado,"camion/es no fueron despachados por falta de naranjas (< 80%)")

def main():
    return ingresarNaranjas()

main()
