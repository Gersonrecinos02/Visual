usuarios = [
        ["chanchito", 4], 
        ["felipe", 1], 
        ["pulga", 5]
]

# nombre = []
# for usuario in usuarios:
#     nombre.append(usuario, 0)
#     print(nombre)

# nombres = [usuario[0] for usuario in usuarios]

# nombre = [expresion for item in items]

# filtrar
# nombres = [usuario for usuario in usuarios if usuario[1] >2]


# filtrar y transformar
# nombres = [usuario [0] for usuario in usuarios if usuario[1] >2]


# nombres = list(map(lambda usuario: usuario[0], usuarios))

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)