#VOLUMEN_AREA_CILINDRO
#{El programa dado como datos el radio y la altura de cilindro, calcula su área y su volumen.}

def area_cilindro():
        
    while True:
        
        print("Bienvenido")
        
        radio = float(input("Ingrese el radio del cilindro: "))
        altura = float(input("Ingrese la altura del cilindro: "))

        if radio > 0:
            volumen = 3.141592 * radio**2 * altura 
        else: 
            print("Ingrese una cantidad valida")


        if altura > 0:
            area = 2* 3.141592 * radio * altura 
        else: 
            print("Ingrese una cantidad valida")

        print(f"El volumen del cilindro es de: {volumen:.2f}")
        print(f"El area del cilindro es de: {area:.2f}")

area_cilindro()