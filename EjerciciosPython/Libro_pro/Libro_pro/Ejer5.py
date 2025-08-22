#{El programa, dados como datos la base y la altura de un
#triángulo, calcula su superficie

def triangulo(base, altura):
    superfice = (base * altura) / 2
    print(f"Su superfice es de: {superfice}")

base=float(input("Ingresa tu base: "))
altura=float(input("Ingresa tu altura: "))

triangulo(base, altura)