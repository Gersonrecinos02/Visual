'''
Calculadora que ingrese dos numeros y que opere todas las operaciones
'''

print("Bienvenido al programa")
print("")

def calculadora():
    while True:
        print("Operaciones")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Salir")

        opcion=int(input("Elige una opcion 1-4: "))

        numero1= int(input("Ingrese un numero"))
        numero2= int(input("Ingrese un numero"))

        if opcion == 4:
            print("Has salido del programa")
            break
        
        if opcion == 1:
            resultado = numero1 + numero2
            print(f"Su resultado es de: {resultado}")
        
        elif opcion == 2: 
            resultado = numero1 - numero2
            print(f"Su resultado es de: {resultado}")
        
        elif opcion == 3:
            resultado = numero1 * numero2
            print(f"Su resultado es de: {resultado}")
        
        else: 
            print("Has ingresado un numero incorrecto")

calculadora()



