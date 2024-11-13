naipes = 13  # Cada palo tiene 12 o 13 cartas
palos = ['oro', 'copa', 'espada', 'basto']

listaNaipes = [
    (str(i) + ' de ' + palo) if i not in [11, 12, 13] else
    ('sota de ' + palo) if i == 11 else
    ('caballo de ' + palo) if i == 12 else
    ('rey de ' + palo)
    for palo in palos for i in range(1, 13)
]


print(listaNaipes)


# no puede haber elif en una lista por comprension
# estructura lista pro comprension = [expresión for elemento in iterable if condición] <- cuando no hay else, si hay else, los condicionales van antes del bucle

# operador ternario: valor_si_verdadero if condicion else valor_si_falso

# se pueden anidar, aunque se puede volver dificil de leer si son muchos
