nombre= input("Ingrese su nombre: ")
edad= int(input("Ingrese su edad: "))
años= int(input("En cuantos años quieres saber tu edad: "))


if edad > 0: 
    edadFutura = int(edad + años) 
    print(f"{nombre} , en {años} años tendras: {edadFutura} ")

else: 
    print("Datos incorrectos")
