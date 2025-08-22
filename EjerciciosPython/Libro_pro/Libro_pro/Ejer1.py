#El algoritmo, dadas cinco calificaciones de un alumno, calcula su promedio

def calificacion(Clase1, Clase2, Clase3, Clase4, Clase5):

    suma = (Clase1 + Clase2 + Clase3 + Clase4 + Clase5)/5
    print(f"El promedio de su calificacion es:  {suma}")         


c1 = float(input("Ingrese la calificación de su primera clase:  "))
c2 = float(input("Ingrese la calificación de su segunda clase:  "))
c3 = float(input("Ingrese la calificación de su tercera clase:  "))
c4 = float(input("Ingrese la calificación de su cuarta clase:  "))
c5 = float(input("Ingrese la calificación de su quinta clase:  "))

calificacion(c1, c2, c3, c4, c5)


