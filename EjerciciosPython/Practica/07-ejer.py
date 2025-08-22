print("Bienvenido")

def salario():
    while True:
        print("Elige a que departamento perteneces: ")
        print("1. Contabilidad")
        print("2. Ventas")
        print("3. Informatica")
        print("4. O escribe -1 para salir")

        departamento = input("Elige un departamento para continuar: ").lower()
        
        if departamento == "-1":
            print("Has salido del programa")
            break

        sueldo = float(input("Ingresa su sueldo: "))
        if departamento == "contabilidad":
            if sueldo > 1000: 
                total = sueldo + (sueldo * 0.10)
            elif sueldo >= 1000 and sueldo < 2000:
                total = sueldo + (sueldo * 0.05)
            elif sueldo >= 2000 and sueldo < 3000:
                total = sueldo + (sueldo * 0.07)
            else: 
                print("Escribe una cantidad correcta")
        elif departamento == "ventas":
            if sueldo > 1000: 
                total = sueldo + (sueldo * 0.10)
            elif sueldo >= 1000 and sueldo < 2000:
                total = sueldo + (sueldo * 0.05)
            elif sueldo >= 2000 and sueldo < 3000:
                total = sueldo + (sueldo * 0.07)
            else: 
                print("Escribe una cantidad correcta")
        elif departamento == "informatica":
            if sueldo > 1000: 
                total = sueldo + (sueldo * 0.10)
            elif sueldo >= 1000 and sueldo < 2000:
                total = sueldo + (sueldo * 0.05)
            elif sueldo >= 2000 and sueldo < 3000:
                total = sueldo + (sueldo * 0.07)
            else: 
                print("Escribe una cantidad correcta")
        else: 
            print("Has ingresado el departamento incorrecto")


        print(total)

salario()