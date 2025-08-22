#{El programa, dado el nombre de un dinosaurio, su peso expresado en toneladas y
#su longitud expresada en libras; escribe el nombre del dinosaurio, su peso y longitud 
#expresadas en kilogramos y metros, respectivamente}

def dinosaurio(nombre, peso, longitud):
    nombre = NombreDino
    pesoKg = peso * 1000
    Metros = longitud * 0.3048
    print(f"El nombre del dinosario: {nombre}")
    print(f"El peso es de: {pesoKg}")
    print(f"Su longitud es de: {Metros}")

NombreDino=input("Ingrese el nombre del dinosaurio: ")
PesoDino=int(input("Ingrese el peso del dinosaurio: "))
LongitudDino=float(input("Ingrese la longitud del dinosario:"))

dinosaurio(NombreDino, PesoDino, LongitudDino)