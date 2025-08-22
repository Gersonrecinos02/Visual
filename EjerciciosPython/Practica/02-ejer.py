nombre = input("Ingrese su nombre: ")
pesoKg= float(input("Ingrese su peso en Kg: "))
altura= float(input("Ingrese su altura en metros: "))

if pesoKg > 0:
    Imc = float(pesoKg / (altura**2)) 
    print(f"{nombre}, tu IMC es de {Imc}")
else:
    print("Datos incorrectos")