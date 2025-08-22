nombre = input("Ingrese su nombre: ")
saldoInicial = 1000

def mostrarMenu():
    print("Bienvenido al Menu: ")
    print("1. Consultar Saldo")
    print("2. Depositar Dinero")
    print("3. Retirar Dinero ")
    print("4. Salir")

def main():
    global saldo
    while  True:
        mostrarMenu()
        opcion = int(input("Selecciona una opcion (1-4): ")) 

        if opcion == 4:
            print("Has salido del sistema")
            break

        if opcion == 1: 
            print(f"Su saldo es de: {saldoInicial}")
        elif opcion == 2:  
                deposito = float(input("Cuanto desea depositar: "))
                if deposito > 0:
                    saldo = deposito + saldoInicial
                    print(f"Su nuevo saldo es de: {saldo}")
                else:
                    print("El saldo debe ser mayor a 0")
        elif opcion == 3:
            retiro = float(input("Ingrese el monto a retirar: "))
            if retiro > 0: 
                saldoNuevo = retiro - saldoInicial
                print(f"Su nuevo saldo es de: {saldoNuevo}")
            else:
                print("Ingrese una cantidad mayor a 0")

        else: 
            print("Ingrese una opcion correcta")

main()