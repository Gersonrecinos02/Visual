numeros = [2, 4, 1, 45, 72, 22]

# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [
        ["chanchito", 4], 
        ["felipe", 1], 
        ["pulga", 5]
]

# def ordena(elemento):
    # return elemento[1]

usuarios.sort(key=lambda el:el[1], reverse=True)
print(usuarios)