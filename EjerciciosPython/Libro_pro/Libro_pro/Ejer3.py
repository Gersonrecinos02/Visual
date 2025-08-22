#{El programa, dado como datos la base y la altura de un rectángulo, calcula su perímetro y superficie}

def rectangulo (base, altura):
    perimetro = 2 * (base + altura)
    superficie = base * altura
    print(f"Su perimetro es de: {perimetro}")
    print(f"Su superficie es de: {superficie}")

num1= float(input("Ingrese su base: "))
num2= float(input("Ingrese su altura: "))
rectangulo(num1, num2)