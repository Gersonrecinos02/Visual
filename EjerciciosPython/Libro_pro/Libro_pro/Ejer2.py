#{El programa, dado como dato un número entero positivo, calcula el cuadrado y el cubo de dicho número}

def numeroent (numero):
    cuadrado = numero **2
    cubo = numero **3
    print(f"Su numero al cuadrado es: {cuadrado}")
    print(f"Su numero al cubo es: {cubo}")


Num1=float(input("Ingrese su numero positivo: "))

numeroent(Num1)
