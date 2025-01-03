mascotas = [
    "pelusa", 
    "canchito", 
    "felipe", 
    "pulga",
    "Wolfgang", 
    "chanchito feliz"
]
mascotas.insert(1, "Melvin")
mascotas.append("Chanchito triste")

mascotas.remove("pulga")
mascotas.pop(1)
del mascotas[0]
mascotas.clear()
print(mascotas)