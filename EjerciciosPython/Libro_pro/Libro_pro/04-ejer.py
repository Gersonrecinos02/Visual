def main():
    while True:
        print("Bienvenido")

        entrada_salida = input("Desea continuar s/n: ").lower().strip()
        
        if entrada_salida == "n":
            print("Has salido del programa")
            break
        if entrada_salida == "s":
            try:
                nota1 = float(input("Ingresa tu nota #1 obtenida: "))
                nota2 = float(input("Ingresa tu nota #2 obtenida: "))
                nota3 = float(input("Ingresa tu nota #3 obtenida: "))
                nota4 = float(input("Ingresa tu nota #4 obtenida: "))
                nota5 = float(input("Ingresa tu nota #5 obtenida: "))


                total = (nota1 + nota2 + nota3 + nota4 + nota5)/5 

                if total >= 6 :
                    print(f"Has aprobado con: {total}")
                elif total < 6:
                    print(f"No has aprobado tu nota es: {total}")
        
            except ValueError:
                print("Escribe un numero correcto")
            
        else:
            print("El programa solo acepta 's' o 'n'. " )        
main()