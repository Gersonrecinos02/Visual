def main():
    while True:

        print("Bienvenido")

        entrada_salida = input("Desea continuar s/n: ").lower().strip()

        if entrada_salida == "n":
            print("Has salido del programa")
            break
        elif entrada_salida == "s":
            
            print("Estas son las claves junto con su respectiva zona")
            print("Clave: 12        Zona: America del norte ")
            print("Clave: 15        Zona: America Central ")
            print("Clave: 18        Zona: America del sur ")
            print("Clave: 19        Zona: Europa ")
            print("Clave: 23        Zona: Asia ")
            print("Clave: 25        Zona: África ")
            print("Clave: 29        Zona: Oceanía ")

            try:
                clave = int(input("Ingrese su clave: "))
            except ValueError: 
                print("Ecribe una clave correta")
            try:       
                minutos = float(input("Ingrese los minutos de su llamada: "))


                if clave == 12:
                    total_minutos = minutos * 2
                elif clave == 15:
                    total_minutos = minutos * 2.2
                elif clave == 18:
                    total_minutos = minutos * 4.5
                elif clave == 19:
                    total_minutos = minutos * 3.5
                elif clave == 23:
                    total_minutos = minutos * 6
                elif clave == 25:
                    total_minutos = minutos * 6
                elif clave == 29:
                    total_minutos = minutos * 5

                print(f"El total de minutos es de: {total_minutos:.1f}")
            except ValueError:
                print("Escribe los minutos correctos...")

main()