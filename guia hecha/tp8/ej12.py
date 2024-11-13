"""
Una librería almacena su lista de precios en un diccionario. Diseñar un programa
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
costoso que venden en el comercio.
"""

def crearDiccionario(listaElementos, listaPrecios):
    try:
        pos = listaElementos.index("cuaderno")
    except ValueError: 
        print("no se encuentra el cuaderno en la lista")
    else:
        listaPrecios[pos] = listaPrecios[pos] * 1.15
    diccionario = {}
    for i in range(len(listaElementos)): 
        diccionario[listaElementos[i]] = listaPrecios[i]

    masCaro = max(listaPrecios)

    print("diccionario de precios ", diccionario)
    print("lista de precios ", listaPrecios, "mas caro", masCaro)
    return diccionario


librerias = [
    "NumPy",
    "Pandas",
    "Matplotlib",
    "Scikit-learn",
    "TensorFlow",
    "Keras",
    "Flask",
    "Django",
    "cuaderno"
]


precios = [
    50.0,  # NumPy
    40.0,  # Pandas
    30.0,  # Matplotlib
    70.0,  # Scikit-learn
    100.0, # TensorFlow
    80.0,  # Keras
    20.0,  # Flask
    90.0,   # Django
    100.0
]

diccionario = crearDiccionario(librerias, precios)