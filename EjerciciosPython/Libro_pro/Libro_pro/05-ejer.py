def main():
    while True: 
        print("Bienvenido")
        
        entrada_salida = input("Ingrese 'continuar' o -'1' para salir:  ").lower().strip()

        if entrada_salida == "-1":
            print("Has salido del programa...")
            break
        
        elif entrada_salida == "continuar":
            try: 

                monto = float(input("Ingresa el monto de compra: "))

                if monto < 500:
                    total = monto
                elif monto <= 1000:
                    total = monto - (monto * 0.05)
                elif monto <= 7000:
                    total = monto - (monto * 0.11)
                elif monto <= 15000:
                    total = monto - (monto * 0.18)
                else:
                    total = monto - (monto * 0.25)


                print(f"El total de compra es de : {total}")
                
            except ValueError:
                print("Escribe una cantidad correcta")

        else:
            print("El programa solo admite 'continuar'  o '-1' para salir. ")
main()