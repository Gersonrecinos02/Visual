print("Bienvenidos a la calculadora")
print("para salir escribe salir")
print("las operaciones son suma, resta, multi, divi")

resultado =""
while True:
    if not resultado: 
        resultado = input("ingrese numero: ")
        if resultado.lower() == "salir":
            break   
        resultado = int(resultado)     
    op = input("Ingresa operacion: ")
    if op.lower() == "salir":
        break
    n2= input("ingresa siguiente numero: ")
    if op.lower() == "salir":
        break
    n2= int(n2)
    
    if op.lower() =="suma":
        resultado += n2
        
    elif op.lower() =="resta":
        resultado -= n2
        
    elif op.lower() =="multi":
        resultado *= n2
        
    elif op.lower() =="divi":
        resultado /= n2
        
    else:
        print("operacion no valida")
        break
    
    print(f"el resultado es {resultado}")

