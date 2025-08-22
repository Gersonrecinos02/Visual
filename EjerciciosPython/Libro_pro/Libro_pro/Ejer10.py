#Galones de gasolina


while True:

    print("Bienvenido")
    print("Escriba ingresar para continuar o salir para cerrar el programa")
    ingreso = input().lower()
    

    if ingreso == "salir":
        print("Has salido del programa")
        break


    if ingreso == "ingresar":
        galones = float(input("Por favor ingrese los galones surtidos: "))
        total = (galones * 3.785) * 8.20
    else:
        print("Escriba una cantidad valida")
    
    
    print(f"El total es de: {total:.2f}")

