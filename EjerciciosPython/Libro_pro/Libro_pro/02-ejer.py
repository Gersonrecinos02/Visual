#{El programa, dado un número determinado de días, calcula cuántos segundos tienen éstos}

def main():
    while True:
    
        print("Bienvenido")
    
        opcion = input("Desea continuar s/n: ").lower()
    
        if opcion == "s":
    
    
            dias = int(input("Ingrese un número de días: "))
    
            if dias > 0:
                segundos_por_dia = 24 * 60 * 60
                segundos_dias = dias * segundos_por_dia
            else: 
                print("Escribe un dia positivo")
        
            print(f"{dias} días tienen {segundos_dias} segundos.")
    
        elif opcion == "n":
            print("Has salido del programa")
            break
main()