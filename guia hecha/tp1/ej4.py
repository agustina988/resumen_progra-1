# Un comercio de electrodomésticos necesita para su línea de cajas un programa que
# le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
# dos números enteros, correspondientes al total de la compra y al dinero recibido.
# Informar cuántos billetes de cada denominación deben ser entregados como vuelto,
# de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes
# de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el
# dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
# de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se
# abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1
# billete de $200, 1 billete de $100 y 3 billetes de $10

# $5000, $1000, $500, $200, $100, $50 y $10.
# Emitir un mensaje de error si el
# dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
# de billetes con denominaciones adecuadas.

def entregarCambio(dineroCosto, dineroRecibido):
    cantDineroCambio = 0
    cambio = 0 
    cambioSinDevolucion = 0
    if dineroRecibido < dineroCosto: 
        print("Dinero insuficiente para realizar el pago ")
    
    else:
        if (dineroRecibido - dineroCosto) > 0:
            cantDineroCambio = dineroRecibido - dineroCosto

            while cantDineroCambio >= 5000: 
                cantDineroCambio -= 5000
                cambio += 5000
            
            while cantDineroCambio >= 1000: 
                cantDineroCambio -= 1000
                cambio += 1000

            while cantDineroCambio >= 500: 
                cantDineroCambio -= 500
                cambio += 500
            
            while cantDineroCambio >= 100: 
                cantDineroCambio -= 100
                cambio += 100

            while cantDineroCambio >= 50: 
                cantDineroCambio -= 50
                cambio += 50
                
            while cantDineroCambio >= 10: 
                cantDineroCambio -= 10
                cambio += 10
                
            if cantDineroCambio > 0: 
                cambioSinDevolucion = cantDineroCambio
                print("desgraciadamente no tenemos denominaciones para devolverle el total de su cambio, tendra un a favor ", cambioSinDevolucion)

    return cambio

dineroCosto = int(input("ingrese el costo del producto "))
dineroRecibido = int(input("Ingrese la cantidad de dinero con la que abonara "))
cambio = entregarCambio(dineroCosto, dineroRecibido)
print("su cambio es ", cambio)