
def main():
    while True:
    
        print("Bienvenido")
    
        entrada_salida= input("Desea continuar s/n: ").lower().strip()

        if entrada_salida == "n":
            print("Has salido del programa")
            break
            
        elif entrada_salida == "s":
            try:
                sueldo = float(input("Ingrese su sueldo: "))
                categoria = int(input("ingrese su categoria: "))
        
                if categoria == 1:
                    total = sueldo + (sueldo * 0.15)
                elif categoria == 2:
                    total = sueldo + (sueldo * 0.10)
                elif categoria == 3: 
                    total = sueldo + (sueldo * 0.08)
                elif categoria == 4:
                    total = sueldo + (sueldo * 0.07)
                else: 
                    print("Escribe un numero dentro de la categoria 1-4. ")
                    continue
            
                print(f"Su categoria es {categoria} y su sueldo es de: {total:.2f}")    
                
            except ValueError:
                print("Error: Escribe un numero dentro de la categoria 1-4. ")
        
        else: 
            print("Escribe 's' o 'n' para continuar")  
    
main()